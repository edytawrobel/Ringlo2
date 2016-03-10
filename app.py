from flask import Flask, render_template
from twilio.rest import TwilioRestClient
import csv
app = Flask(__name__)

@app.route("/landingPage")
def landingPage():
    return render_template("index.html")


@app.route("/send", methods=['POST'])
def send():

# Your Account Sid and Auth Token from twilio.com/user/account
    account_sid = "AC651dcd0b578ee9f523abfb0de332b948"
    auth_token  = "c65b08717f3dd6727a4c845809088cb8"
    client = TwilioRestClient(account_sid, auth_token)

    message = client.messages.create(body="Jenny please?! I love you <3",
        to="+447853263417",    # Replace with your phone number
        from_="+441278393077") # Replace with your Twilio number
    print message.sid

    smss = client.sms.messages.list()
    import pdb; pdb.set_trace()

    #with open('my_csv.csv', 'w') as f:
        #writer = csv.Writer()
        #for sms in smss:
            #writer.write(sms.to, sms.from_, sms.message)


    #https://api.twilio.com/2010-04-01/Accounts/AC651dcd0b578ee9f523abfb0de332b948/SMS/Messages.csv?PageSize=1000
    # export the raw data of messages from twilio

@app.route('/signup.html', methods=['POST'])
def signup():

    global _name
    global _email
    global _city

    _sendTo = request.form['inputEmail']

    requests.post(
        "https://api.mailgun.net/v3/sandbox4b9b1d94381b48b4b05732cffa0da0ac.mailgun.org/messages",
        auth=("api", "key-6c19c1c364273bc85bb70777ef854618"),
        data={"from": "Mailgun Sandbox <postmaster@sandbox4b9b1d94381b48b4b05732cffa0da0ac.mailgun.org>",
              "to": "User <"+_sendTo+">",
              "subject": "User details",
              "html": "<iframe src="++" width='150px' height='150px' allowFullScreen></iframe>" +
                      "This is a message from "+_name+" from "+_city+", "

    }
    )

if __name__ == "__main__":
    app.run()
