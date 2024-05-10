from gtts import gTTS
from flask import Flask, send_file, send_from_directory
from googletrans import Translator
import os
#pip install googletrans==4.0.0rc1

app = Flask(__name__)
countNo = 0
countYes = 0



@app.route("/")
def hello_world():
    return "<p>API running! Here's our website</p>" + f'The amount of votes for yes is {countYes} and the amount of votes for no is {countNo}'

@app.route("/count/<YesNo>", methods=['GET'])
def resultsCount(YesNo= None):
    global countYes, countNo
    if int(YesNo) == 1:
        countYes += 1
    else:
        countNo += 1
    text = f'The amount of votes for yes is {countYes} and the amount of votes for no is {countNo}'
    obj = gTTS(text=text, slow=False)
    obj.save('registeredVotes.wav')
    return send_file('registeredVotes.wav')


@app.route("/speak/<lang>/<firstOption>/<secondOption>", methods=['GET'])
def resultsSpoken(firstOption = None, secondOption = None, lang="en"):
    winner_text = "first option" if int(firstOption) > int(secondOption) else "second option"
    winner_number = firstOption if int(firstOption) > int(secondOption) else secondOption
    loser_number = secondOption if int(firstOption) > int(secondOption) else firstOption
    text = f'The winner of the vote is the {winner_text}, with {winner_number} votes compared to {loser_number} votes'
    translator = Translator()
    translation = translator.translate(text, src='en', dest=lang)
    print(translation.text)
    obj = gTTS(text=translation.text, slow=False, lang=lang)
    obj.save('translation.wav')
    return send_file('translation.wav')

@app.route("/vxml_yes")
def voteyes():
    return send_from_directory(app.static_folder, 'vote_yes.vxml')

@app.route("/voice")
def voteVoice():
    filepath = 'audio/registeredVotes.wav'
    if os.path.isfile(filepath):
        return open('audio/registeredVotes.wav', "r")
    else:
        console.log("Error")

@app.route("/voteNo")
def voteno():
    return send_from_directory(app.static_folder, 'vote_no.vxml')
