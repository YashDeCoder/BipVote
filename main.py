from gtts import gTTS
from flask import Flask, send_file
from googletrans import Translator
#pip install googletrans==4.0.0rc1

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>API running! Here's our website</p>"


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
