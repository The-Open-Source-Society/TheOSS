from flask import Flask, render_template, request
from wtforms import Form, BooleanField, StringField, PasswordField, validators
from flask_wtf import FlaskForm
from wtforms.validators import InputRequired, Email, Length

class LoginForm(FlaskForm):
    username = StringField('Username', validators =[InputRequired(), Length(min=4, max=50)])
    password = PasswordField('Password', validators =[InputRequired(), Length(min=8, max=80)])
    remember = BooleanField('remember me') 

class RegisterForm(FlaskForm):
     username = StringField('Username', validators =[InputRequired(), Length(min=4, max=50)])
     email = StringField('Email ID', validators = [InputRequired(), Email(message='Invalid email'), Length(max=50)]) 
     password = PasswordField('Password', validators =[InputRequired(), Length(min=8, max=80)])

app = Flask(__name__)

@app.route("/")
def signin():

    return render_template("toss.html")

@app.route("/contact")
def contact():
    
    return "stheopensource@gmail.com"

if __name__ == '__main__':
    app.run(debug=True)
