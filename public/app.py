from flask import Flask, render_template, request

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

@app.route("/contact")
def contact():
    
    return "stheopensource@gmail.com"

if __name__ == '__main__':
    app.run(debug=True)
