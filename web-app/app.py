from flask import Flask, request, render_template, flash, redirect, url_for
import os
import uuid
import time
from music_analysis.analyse import analyse
from gen_art.generate_art import generate
from definitions import ROOT_DIR

ALLOWED_EXTENSIONS = {'mp3', 'wav'}

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 20 * 1024 * 1024  # 20MB
app.config['UPLOAD_FOLDER'] = os.path.join(ROOT_DIR, 'web-app/static/upload')
app.secret_key = 'q=Lxcbh59T!hA_0Qv%Eb'


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@app.route('/process', methods=['POST'])
def process():

    generated_img_folder = os.path.join(ROOT_DIR, 'web-app/static/img/generated')
    now = time.time()
    for f in os.listdir(generated_img_folder):
        f = os.path.join(generated_img_folder, f)
        if os.stat(f).st_mtime < now - 10:
            os.remove(f)
    for f in os.listdir(app.config['UPLOAD_FOLDER']):
        f = os.path.join(app.config['UPLOAD_FOLDER'], f)
        if os.stat(f).st_mtime < now - 10:
            os.remove(f)

    print("Took ", time.time() - now, "s cleaning up folders")

    if 'file' not in request.files:
        flash('No file part - select a file!')
        return redirect(url_for('index'))
    f = request.files['file']
    if f.filename == '':
        flash('No selected file')
        return redirect(url_for('index'))
    filename = f.filename
    if f and allowed_file(filename):
        filename = uuid.uuid4().hex + os.path.splitext(f.filename)[1]
        print(filename)
        f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    else:
        flash('File name not allowed')
        return redirect(url_for('index'))

    happy, dance, aggressive, chill, acoustic = analyse(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    output_filename = uuid.uuid4().hex + '.png'
    output_path = os.path.join(generated_img_folder, output_filename)
    generate(output_path, happy, dance, aggressive, chill, acoustic)
    return render_template('display-image.html', filename=output_filename)


@app.route('/display/<filename>')
def display_image(filename):
    return redirect(url_for('static', filename='img/generated/' + filename), code=301)


if __name__ == '__main__':
    app.run()
