from random import random

from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "Hello!"


@app.route("/rand")
def rand():
    r = random()
    if r < 0.3:
        return f"{r=:.3f} smaller"
    elif r <= 0.7:
        return f"{r=:.3f} medium"
    else:
        return f"{r=:.3f} larger"
