from flask import Flask, render_template, flash, request, redirect, url_for, session, logging
app = Flask(__name__)
from wtforms import Form, StringField, TextAreaField, PasswordField, validators
from encrypt import Encrypt
from decrypt import Decrypt
class EncryptForm(Form):
    text = TextAreaField("Plain Text: ", [validators.DataRequired()])

@app.route("/")
def index():
    return render_template("home.html")

@app.route("/encrypt", methods=["GET", "POST"])
def encrypt():
    form = EncryptForm(request.form)
    if request.method == "POST" and form.validate():
        text = form.text.data
        print(text)
        return render_template("encrypt.html", form=form)
    return render_template("encrypt.html", form=form)



if __name__ == "__main__":
    app.run(debug=True)
