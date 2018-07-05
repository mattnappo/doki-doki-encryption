from flask import Flask, render_template, flash, request, redirect, url_for, session, send_from_directory, logging
UPLOAD_FOLDER = 'static/uploads/'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'txt'])
app = Flask(__name__, static_url_path='/static')
from wtforms import Form, StringField, TextAreaField, PasswordField, validators, FileField
from werkzeug.utils import secure_filename
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
import random, os, cleaner
cleaner.clean("static")
from encrypt import Encrypt
from decrypt import Decrypt
class EncryptForm(Form):
    text = TextAreaField("", [validators.DataRequired()])
@app.route("/")
def index():
    return render_template("home.html")

@app.route("/encrypt", methods=["GET", "POST"])
def encrypt():
    form = EncryptForm(request.form)
    if request.method == "POST" and form.validate():
        text = form.text.data
        file_name = str(random.random())[2:]
        Encrypt(
            text,
            "static/encrypted/" + file_name,
            "png"
        )
        session['filename'] = file_name
        return render_template("encrypt.html", form=form)
    session['filename'] = ''
    return render_template("encrypt.html", form=form)
def allowed_file(filename):
    return '.' in filename and \
            filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
@app.route('/decrypt', methods=['GET', 'POST'])
def upload_file():
    session['filename'] = ""
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files :
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            PATH = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(PATH)
            session['filename'] = filename
            text = ""
            with open(Decrypt(PATH).NAME, "r") as f:
                text = f.read()
            print(text)
            return render_template("decrypt.html", text=text)
    else:
        session['filename'] = ""
    return render_template("decrypt.html")
@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)
if __name__ == "__main__":
    app.secret_key = 'super secret key'
    app.run(host= '0.0.0.0', debug=True)
