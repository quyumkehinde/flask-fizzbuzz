from flask import Flask, render_template

app = Flask(__name__)


@app.get("/fizzbuzz")
def index():
    return render_template("fizzbuzz.html")
