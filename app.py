from flask import Flask, render_template, request, flash

app = Flask(__name__) # create a class for app
app.secret_key = "viniciusf"

@app.route("/hello")
def index():
    flash("what`s your name?")
    return render_template("index.html")

@app.route("/greet", methods=["POST", "GET"])
def greet():
    flash("Hi " + str(request.form['name_input']) + ", great to see you!") #the name_input must match with html file
    return render_template("index.html")
