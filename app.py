from flask import Flask, render_template, request
from twilio.rest import TwilioRestClient
import unicodecsv
import requests
import json
import urllib


app = Flask(__name__)

@app.route("/landingPage")
def landingPage():
    return render_template("index.html")


@app.route("/send", methods=['POST'])
def send():
    print "sent text"

@app.route("/signup", methods=['POST'])
def signup():
    return render_template('signup.html')


@app.route("/thankYou", methods=['POST'])
def thankYou():

    global _name
    global _email
    global _city
    global _season
    global _giphy

    # read the posted values from the UI
    _name = request.form['inputName']
    _email = request.form['inputEmail']
    _city = request.form['inputCity']
    _season = request.form['inputSeason']


    # Giphy https://github.com/Giphy/GiphyAPI
    data = json.loads(urllib.urlopen("http://api.giphy.com/v1/gifs/search?q=ryan+gosling&api_key=dc6zaTOxFJmzC&limit=5").read())
    _giphy = "http://api.giphy.com/v1/gifs/random?fmt=html&tag={}&api_key=dc6zaTOxFJmzC".format(_season)

    # validate the received values
    if _name and _email and _city and _season:
        print "All good!"
    else:
        return json.dumps({'html':'<span>Enter the required fields</span>'})


    _sendTo = request.form['inputEmail']

    req = requests.post(
        "https://api.mailgun.net/v3/sandboxe8185892477b4f77bfa603cb9a41c23a.mailgun.org/messages",
        auth=("api", "key-79dff1cbbecadfc27a0684b7c83e576c"),
        data={"from": "Ringlo Team <mailgun@sandboxe8185892477b4f77bfa603cb9a41c23a.mailgun.org>",
              "to": _sendTo,
              "subject": "Newsletter Signup",
              "html": "<iframe src="+_giphy+" width='150px' height='150px' allowFullScreen></iframe>" +
                      "This is a message from "+_name+" from "+_city+", " +
                      "where it looks like: "+_season

    })

    print req

    return render_template("thankYou.html") #Confirmation page

@app.route("/messagesent", methods=['POST'])
def send():


# Your Account Sid and Auth Token from twilio.com/user/account
    account_sid = "AC651dcd0b578ee9f523abfb0de332b948"
    auth_token  = "c65b08717f3dd6727a4c845809088cb8"
    client = TwilioRestClient(account_sid, auth_token)

    message = client.messages.create(body="I'm currently walking down a dim lit area. Please stay in touch with me.",
        to="+447853263417",    # Replace with your phone number
        from_="+441278393077") # Replace with your Twilio number
    print message.sid



   # def smslist(sms_messages):
    #    with open(sms_messages) as csvfile:
     #       reader = unicodecsv.DictReader(sms_messages)

      #      for row in reader:
       #         print row Direction
        #        print row DateSent
         #       print row To
          #      print row From
           #     print row Body

    # smslist('sms_messages.csv')


    #https://api.twilio.com/2010-04-01/Accounts/AC651dcd0b578ee9f523abfb0de332b948/SMS/Messages.csv?PageSize=1000
    # export the raw data of messages from twilio

    # get a list of all the sms messages from twilio
    smss = client.sms.messages.list()

    # writes all the sms messages into a csv file
    with open('my_smslist.csv', 'w') as f:

        writer = csv.DictWriter(f, fieldnames=["date_sent", "body", "from_", "to"])
        writer.writeheader()
        for sms in smss:
            writer.writerow({"date_sent": sms.date_sent, "body": sms.body, "from_": sms.from_, "to": sms.to})
            print sms.date_sent, sms.body, sms.from_, sms.to

    return render_template('messagesent.html')

    #https://api.twilio.com/2010-04-01/Accounts/AC651dcd0b578ee9f523abfb0de332b948/SMS/Messages.csv?PageSize=1000
    # export the raw data of messages from twilio

    # import pdb; pdb.set_trace()

@app.route("/dataanalysis")
def dataAnalysis():
    with open('my_smslist.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        data = list(reader)
    print data
    return render_template("dataanalysis.html", grid=data) #Police UI Data Analysis Page

if __name__ == "__main__":
    app.run(debug=True)
