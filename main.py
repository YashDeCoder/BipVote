from gtts import gTTS
from flask import Flask, send_file, send_from_directory, request
from googletrans import Translator
import os
#pip install googletrans==4.0.0rc1

app = Flask(__name__)

def save_number_to_file(number, filename):
    with open(filename, 'a') as file:
        file.write(str(number) + '\n')

def read_last_number_from_file(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        if lines:
            return int(lines[-1].strip())
        else:
            return None

def reset_files(*filenames):
    for filename in filenames:
        with open(filename, 'w') as file:
            file.write('0\n')

# Home page
@app.route("/")
def hello_world():
    countNo = read_last_number_from_file('votesYes.txt')
    countYes = read_last_number_from_file('votesNo.txt')
    return "<p>API running! Here's our website</p>" + f'The amount of votes for yes is {countYes} and the amount of votes for no is {countNo}'

# Registering a vote
@app.route("/count/<YesNo>", methods=['GET'])
def resultsCount(YesNo= None):
    countYes = read_last_number_from_file('votesYes.txt')
    countNo = read_last_number_from_file('votesNo.txt')
    if int(YesNo) == 1:
        countYes += 1
    else:
        countNo += 1
    text = f'The amount of votes for yes is {countYes} and the amount of votes for no is {countNo}'
    obj = gTTS(text=text, slow=False)
    obj.save('registeredVotes.wav')
    return send_file('registeredVotes.wav')

# Reset the votes
@app.route("/reset/<lang>", methods=['GET'])
def resultsSpoken(lang="en"):
    firstOption = read_last_number_from_file('votesYes.txt')
    secondOption = read_last_number_from_file('votesNo.txt')
    winner_text = "first option" if int(firstOption) > int(secondOption) else "second option"
    winner_number = firstOption if int(firstOption) > int(secondOption) else secondOption
    loser_number = secondOption if int(firstOption) > int(secondOption) else firstOption
    reset_files('votesNo.txt', 'votesYes.txt')
    text = f'The winner of the vote is the {winner_text}, with {winner_number} votes compared to {loser_number} votes'
    translator = Translator()
    translation = translator.translate(text, src='en', dest=lang)
    print(translation.text)
    obj = gTTS(text=translation.text, slow=False, lang=lang)
    obj.save('winner.wav')
    return send_file('winner.wav')


# To get wav files for certain audio
@app.route("/voice")
def voteVoice():
    enText = "Press 1 for English. Press 2 for French."
    frText = "Appuyez sur 1 pour l'anglais. Appuyez sur 2 pour le français."
    obj = gTTS(text=enText, slow=False, lang='en')
    obj.save('audio/enChoice.wav')
    obj = gTTS(text=frText, slow=False, lang='fr')
    obj.save('audio/frChoice.wav')
    return send_file('audio/frChoice.wav')

# Hosting VXML files 
@app.route("/voteNo")
def voteno():
    return send_from_directory(app.static_folder, 'vote_no.vxml')

@app.route("/vxml_yes")
def voteyes():
    number = str(request.args.get('session.callerid'))
    # making number a hash value
    hashedNum = hash(number)
    save_number_to_file(hashedNum, 'votes_nums.txt')
    return send_from_directory(app.static_folder, 'vote_yes.vxml')