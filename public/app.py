from flask import Flask, render_template, request
import firebase_admin
from firebase import firebase
from firebase_admin import credentials, firestore
cred = credentials.Certificate("/home/arkaprabha/Desktop/theoss-a4460-firebase-adminsdk-hh09p-fd5a411e88.json")
default_app = firebase_admin.initialize_app(cred)
db = firestore.client()

app = Flask(__name__)

@app.route("/")
def home():

    return render_template("toss.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/login_val", methods =["GET","POST"])
def login_valid():
    username = request.form.get('username')
    password = request.form.get('password')
    return " Welcome username : {} ".format(username)

@app.route("/signup")
def signin():
    return render_template("signup.html")

@app.route("/signup_val", methods =["GET","POST"])
def signin_valid():
    username = request.form.get('name')
    password = request.form.get('password')
    email = request.form.get('email')
    s = str(username)
    doc_ref = db.collection("User").document(s)
    doc_ref.set({'Name':username,'Email':email,'Password':password})
    return " Welcome username : {} ".format(username)

@app.route("/contact")
def contact():
    
    return "stheopensource@gmail.com"

if __name__ == '__main__':
    app.run(debug=True)
