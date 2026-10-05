from random import random

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return "Hello!"


@app.route("/rand")
def rand():
    r = random()
    if r < 0.3 :
        return f"{r=:.3f} smaller"
    elif r <= 0.7:
        return f"{r=:.3f} medium"
    else:
        return f"{r=:.3f} larger"

@app.route("/template")
def template():
    return render_template("template.html",greeting="hello")