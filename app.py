from flask import Flask, render_template, request
import twilio
from twilio.rest import Client
import random

quoteList = ["You don’t have to control your thoughts. You just have to stop letting them control you. — Dan Millman",
                "There is a crack in everything, that’s how the light gets in. ― Leonard Cohen",
                "Deep breathing is our nervous system’s love language. — Dr. Lauren Fogel Mersy",
                "I think it’s really important to take the stigma away from mental health… My brain and my heart are really important to me. I don’t know why I wouldn’t seek help to have those things be as healthy as my teeth. —Kerry Washington, from HuffPost",
                "It is not the bruises on the body that hurt. It is the wounds of the heart and the scars on the mind. — Aisha Mirza",
                "Mental health…is not a destination, but a process. It’s about how you drive, not where you’re going. — Noam Shpancer, PhD",
                "Not until we are lost do we begin to understand ourselves. ― Henry David Thoreau",
                "You are not your illness. You have an individual story to tell. You have a name, a history, a personality. Staying yourself is part of the battle. — Julian Seifter",
                "Happiness can be found even in the darkest of times, if one only remembers to turn on the light. — Albus Dumbledore",
                "Vulnerability sounds like truth and feels like courage. Truth and courage aren’t always comfortable, but they're never weakness. — Brené Brown"]

quoteOfSession= random.choice(quoteList)

def sendMessages(number, name, quote):
    account_sid = 'x'
    auth_token = 'x'
    client = Client(account_sid, auth_token)
    client.messages.create(
        body= "Hey Friend, \n\nMirror Mirror in my hand, who is the fairest in the land? You are! You have been linked to a wellness chain. Please send this message to at least 3 other people to encourage self love in your community today. \n\nThe quote of the day is: \n\n" + quote + " \n\nInterested in more self-esteem boosting content? Check out MirrorMirror!",
        from_='+18882071473',
        to=number
        )

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', quote=quoteOfSession)

@app.route("/detector")
def detector():
    return render_template("detector.html")

@app.route("/sent", methods =["GET", "POST"])
def sent():
    if request.method == "POST":
       name = request.form.get("fname")
       receiver = request.form.get("number")
       print(name)
       sendMessages(receiver,name,quoteOfSession)
    return render_template("sent.html")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=2006)