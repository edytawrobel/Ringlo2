from flask import Flask, render_template
from twilio.rest import TwilioRestClient
import csv
app = Flask(__name__)

@app.route("/landingPage")
def landingPage():
    return render_template("index.html")


@app.route("/signup", methods=['POST'])
def signup():
    return render_template('signup.html')

    global _name
    global _email
    global _city
    global _season
    global _giphy

    # read the posted values from the UI
    _name = request.form['inputName']
    _email = request.form['inputEmail']
    _city = request.form['inputCity']
    _animal = request.form['inputSeason']


    # Giphy https://github.com/Giphy/GiphyAPI
    data = json.loads(urllib.urlopen("http://api.giphy.com/v1/gifs/search?q=ryan+gosling&api_key=dc6zaTOxFJmzC&limit=5").read())
    _giphy = "http://api.giphy.com/v1/gifs/random?fmt=html&tag={}&api_key=dc6zaTOxFJmzC".format(_season)

    # validate the received values
    if _name and _email and _city and _season:
        print "All good!"
    else:
        return json.dumps({'html':'<span>Enter the required fields</span>'})


    _sendTo = request.form['inputEmail']

    requests.post(
        "https://api.mailgun.net/v3/sandbox4b9b1d94381b48b4b05732cffa0da0ac.mailgun.org/messages",
        auth=("api", "key-6c19c1c364273bc85bb70777ef854618"),
        data={"from": "Ringlo Team <postmaster@sandbox4b9b1d94381b48b4b05732cffa0da0ac.mailgun.org>",
              "to": "User <"+_sendTo+">",
              "subject": "Newsletter Signup",
              "html": "<iframe src="+_giphy+" width='150px' height='150px' allowFullScreen></iframe>" +
                      "This is a message from "+_name+" from "+_city+", " +
                      "where it looks like: "+_season

    })

@app.route("/thankYou")
def thankYou():
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

    # get a list of all the sms messages from twilio
    smss = client.sms.messages.list()

    # writes all the sms messages into a csv file
    with open('my_smslist.csv', 'w') as f:
        writer = csv.writer(f)
        for sms in smss:
            writer.writerow([sms.date_sent, sms.body, sms.from_, sms.to])
            print sms.date_sent, sms.body, sms.from_, sms.to

    #return render_template('messagesent.html', _name=_name)

    #https://api.twilio.com/2010-04-01/Accounts/AC651dcd0b578ee9f523abfb0de332b948/SMS/Messages.csv?PageSize=1000
    # export the raw data of messages from twilio

    # import pdb; pdb.set_trace()

if __name__ == "__main__":
    app.run(debug=True)
