from gtts import gTTS
from flask_cors import cross_origin
from flask import Flask, send_file, send_from_directory, request, jsonify
from googletrans import Translator
import os
#pip install googletrans==4.0.0rc1

app = Flask(__name__)

## HOME PAGE
@app.route("/")
@cross_origin()
def hello_world():
    countYes, countNo = current_vote()
    return jsonify({
        "result": "<p>API running! Here's our website</p>" + f'The amount of votes for yes is {countYes} and the amount of votes for no is {countNo}', 
    })

## AUXILLIARY METHODS
# Getting the current amount of votes
def current_vote():
    countYes = read_last_number_from_file('votes/votes_yes.txt')
    countNo = read_last_number_from_file('votes/votes_no.txt')
    return countYes, countNo

# Save the vote
def save_number_to_file(number, filename):
    with open(filename, 'a') as file:
        file.write(str(number) + '\n')

# Reading the most recent count
def read_last_number_from_file(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        if lines:
            return int(lines[-1].strip())
        else:
            return None

# Reset all text files
def reset_files(*filenames):
    for filename in filenames:
        with open(filename, 'w') as file:
            if (filename != 'votes/votes_nums.txt'):
                file.write('0\n')

# Making number a hash value
def hash_number(number):
    hashedNum = hash(number)
    with open('votes/votes_nums.txt', 'r') as file:
        for line in file:
            if str(hashedNum) in line.strip():
                return True
    save_number_to_file(hashedNum, 'votes/votes_nums.txt')
    return False

# Registering a vote
def register_count(YesNo, number):
    yes, no = current_vote()
    if hash_number(number):
        return False
    if int(YesNo) == 1:
        yes += 1
        save_number_to_file(yes,'votes/votes_yes.txt')
    else:
        no += 1
        save_number_to_file(no,'votes/votes_no.txt')
    return True

## HTTP REQUESTS
# Reset the votes
@app.route("/reset/<lang>", methods=['GET'])
def results_reset(lang="en"):
    firstOption = read_last_number_from_file('votes/votes_yes.txt')
    secondOption = read_last_number_from_file('votes/votes_no.txt')
    winner_text = "first option" if int(firstOption) > int(secondOption) else "second option"
    winner_number = firstOption if int(firstOption) > int(secondOption) else secondOption
    loser_number = secondOption if int(firstOption) > int(secondOption) else firstOption
    text = f'The winner of the vote is the {winner_text}, with {winner_number} votes compared to {loser_number} votes'
    translator = Translator()
    translation = translator.translate(text, src='en', dest=lang)
    obj = gTTS(text=translation.text, slow=False, lang=lang)
    obj.save('audio/winner.wav')
    reset_files('votes/votes_no.txt', 'votes/votes_yes.txt', 'votes/votes_nums.txt')
    return send_file('audio/winner.wav')

@app.route("/votes/<lang>", methods=['GET'])
def result_voice(lang="en"):
    countYes, countNo = current_vote()
    text = f'The amount of votes for yes is {countYes} and the amount of votes for no is {countNo}'
    translator = Translator()
    translation = translator.translate(text, src='en', dest=lang)
    obj = gTTS(text=translation.text, slow=False, lang=lang)
    obj.save('audio/registeredVotes.wav')
    return send_file('audio/registeredVotes.wav')

## HOSTING VXML FILES 
@app.route("/vxml_no")
def voteno():
    number = str(request.args.get('session.callerid'))
    register_count(0, number)
    return send_from_directory(app.static_folder, 'voters/vote_no.vxml')

@app.route("/vxml_yes")
def voteyes():
    number = str(request.args.get('session.callerid'))
    register_count(1, number)
    return send_from_directory(app.static_folder, 'voters/vote_yes.vxml')

@app.route("/vxml_organizers")
def organizers():
    return send_from_directory(app.static_folder, "organizers/organizers.vxml")

@app.route("/organizers_en")
def en_organizers():
    return send_from_directory(app.static_folder, "organizers/englishMenu.vxml")

@app.route("/organizers_fr")
def fr_organizers():
    return send_from_directory(app.static_folder, "organizers/frenchMenu.vxml")

## HOSTING AUDIO FILES
@app.route("/language_choice")
def language_choice():
    return send_file("audio/languageChoice.wav")

@app.route("/winner")
def winner():
    return send_file("audio/winner.wav")

@app.route("/amount_count")
def votes():
    send_from_directory('audio', "registeredVotes.wav")

@app.route("/frMain")
def fr_main():
    return send_file("audio/frMain.wav")

@app.route("/frFetchVotes")
def fr_fetch_votes():
    return send_file("audio/frFetchVotes.wav")

@app.route("/frResetVotes")
def fr_reset_votes():
    return send_file("audio/frResetVotes.wav")


# To get wav files for certain audio
@app.route("/voice")
def voteVoice():
    text = "The vote is being reset..."
    translator = Translator()
    translation = translator.translate(text, src='en', dest="fr")
    obj = gTTS(text=translation.text, slow=False, lang="fr")
    obj.save('audio/frResetVotes.wav')
    return send_file('audio/frResetVotes.wav')