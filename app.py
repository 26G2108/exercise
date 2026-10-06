from random import random

from flask import Flask, render_template

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


@app.route("/template")
def template():
    return render_template("template.html", greeting="hello", title="あいさつ")


@app.route("/template_list")
def template_list():
    students = []
    for n in range(1, 101):
        students.append(f"2xG2{n:03d}")
    return render_template("template_list.html", students=students, title="学生番号リスト")
