
from flask import Flask, render_template, request, redirect, url_for
import firebase_admin

import requests
import json
import os
os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'



GOOGLE_CLIENT_ID = "351414881625-vic74n66h8t6l5npsd1jooc39tqce7uo.apps.googleusercontent.com"
GOOGLE_CLIENT_SECRET = "SwcaRytS4y0tghchcOyOq3BI"
GOOGLE_DISCOVERY_URL = (
    "https://accounts.google.com/.well-known/openid-configuration"
)


# cred = credentials.Certificate("/home/arkaprabha/Desktop/theoss-a4460-firebase-adminsdk-hh09p-fd5a411e88.json")
# default_app = firebase_admin.initialize_app(cred)
# db = firestore.client()

from flask import Flask, render_template, request


try:
    from firebase import firebase
    from firebase_admin import credentials, firestore
    from oauthlib.oauth2 import WebApplicationClient
    cred = credentials.Certificate("/home/arkaprabha/Desktop/theoss-a4460-firebase-adminsdk-hh09p-fd5a411e88.json")

    default_app = firebase_admin.initialize_app(cred)
    db = firestore.client()
except:
    pass
app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY") or os.urandom(24)
client = WebApplicationClient(GOOGLE_CLIENT_ID)

def get_google_provider_cfg():
    return requests.get(GOOGLE_DISCOVERY_URL).json()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/sign")
def home():
    return render_template("toss.html")

@app.route("/login")
def login():
       return render_template("login.html")

@app.route("/login_with_google")
def logingoogle():
    google_provider_cfg = get_google_provider_cfg()
    authorization_endpoint = google_provider_cfg["authorization_endpoint"]
    request_uri = client.prepare_request_uri(
        authorization_endpoint,
        redirect_uri=request.base_url + "/callback",
        scope=["openid", "email", "profile"],
    )
    return redirect(request_uri)

@app.route("/login_with_google/callback")
def callback():
    code = request.args.get("code")
    google_provider_cfg = get_google_provider_cfg()
    token_endpoint = google_provider_cfg["token_endpoint"]
    token_url, headers, body = client.prepare_token_request(token_endpoint,authorization_response=request.url,
    redirect_url=request.base_url, code = code)
    token_response = requests.post(
    token_url,
    headers=headers,
    data=body,
    auth=(GOOGLE_CLIENT_ID, GOOGLE_CLIENT_SECRET))
    client.parse_request_body_response(json.dumps(token_response.json()))
    userinfo_endpoint = google_provider_cfg["userinfo_endpoint"]
    uri, headers, body = client.add_token(userinfo_endpoint)
    userinfo_response = requests.get(uri, headers=headers, data=body)
    if userinfo_response.json().get("email_verified"):
      users_email = userinfo_response.json()["email"]
      picture = userinfo_response.json()["picture"]
      users_name = userinfo_response.json()["given_name"]
      return "Successfull"
    else:
      return "User email not available or not verified by Google.", 400
    return redirect(url_for("home"))



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
    s = str(email)
    doc_ref = db.collection("User").document(s)
    doc_ref.set({'Name':username,'Email':email,'Password':password})
    return " Welcome username : {} ".format(username)


@app.route("/signup_with_google")
def signupgoogle():
    google_provider_cfg = get_google_provider_cfg()
    authorization_endpoint = google_provider_cfg["authorization_endpoint"]
    request_uri = client.prepare_request_uri(
        authorization_endpoint,
        redirect_uri=request.base_url + "/callback",
        scope=["openid", "email", "profile"],
    )
    return redirect(request_uri)

@app.route("/signup_with_google/callback")
def signupcallback():
    code = request.args.get("code")
    google_provider_cfg = get_google_provider_cfg()
    token_endpoint = google_provider_cfg["token_endpoint"]
    token_url, headers, body = client.prepare_token_request(token_endpoint,authorization_response=request.url,
    redirect_url=request.base_url, code = code)
    token_response = requests.post(
    token_url,
    headers=headers,
    data=body,
    auth=(GOOGLE_CLIENT_ID, GOOGLE_CLIENT_SECRET))
    client.parse_request_body_response(json.dumps(token_response.json()))
    userinfo_endpoint = google_provider_cfg["userinfo_endpoint"]
    uri, headers, body = client.add_token(userinfo_endpoint)
    userinfo_response = requests.get(uri, headers=headers, data=body)
    if userinfo_response.json().get("email_verified"):
      users_email = userinfo_response.json()["email"]
      picture = userinfo_response.json()["picture"]
      users_name = userinfo_response.json()["given_name"]
      s = str(users_email)
      doc_ref = db.collection("User").document(s)
      doc_ref.set({'Name':users_name,'Email':users_email,'Password':users_name})
      return " Welcome username : {} ".format(users_name)
    else:
      return "User email not available or not verified by Google.", 400
    return redirect(url_for("home"))

@app.route("/contact")
def contact():
    
    return "stheopensource@gmail.com"

if __name__ == '__main__':
    app.run(debug=True)
