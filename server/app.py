from flask import Flask, request, render_template
import requests
from music_analysis.analyse import analyse
from gen_art.generate_art import generate
import os
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@app.route('/process', methods=['POST'])
def process():
    try:
        audio_url = request.form['audio-url']
        r = requests.get(audio_url)
        open('audio_files/temp.mp3', 'wb').write(r.content)
    except:
        return "Could not open audio url"

    os.chdir("..")
    happy, dance, aggressive, chill, acoustic = analyse('server/audio_files/temp.mp3')
    generate("server/out_imgs/" + "temp.png", happy, dance, aggressive, chill, acoustic)
    return "done!"


if __name__ == '__main__':
    app.run()