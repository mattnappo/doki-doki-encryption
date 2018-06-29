from flask import Flask, render_template, flash, request, redirect, url_for, session, logging
app = Flask(__name__, static_url_path='/static')
from wtforms import Form, StringField, TextAreaField, PasswordField, validators
import random, settings
from encrypt import Encrypt
class EncryptForm(Form):
    text = TextAreaField("", [validators.DataRequired()])
@app.before_request
def make_session_permanent():
    session.permanent = True
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
            "static/img/" + file_name,
            "png"
        )
        settings.init()
        settings.test()
        print(settings.globals[0])
        session['filename'] = file_name
        return render_template("encrypt.html", form=form)
    session['filename'] = ''
    return render_template("encrypt.html", form=form)


if __name__ == "__main__":
    app.secret_key = 'super secret key'
    app.run(debug=True)
