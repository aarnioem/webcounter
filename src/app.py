from flask import Flask, redirect, render_template, request
from counter import Counter

app = Flask(__name__)
cnt = Counter()

@app.route("/")
def index():
    return render_template("index.html", value=cnt.value)

@app.route("/increment", methods=["POST"])
def increment():
    cnt.increase()
    return redirect("/")

@app.route("/reset", methods=["POST"])
def reset():
    cnt.reset()
    return redirect("/")

@app.route("/set", methods=["POST"])
def set_counter():
    new_value = request.form.get("value")
    try:
        if int(new_value) < 0:
            return "Invalid value"
        cnt.set_counter(int(new_value))
    except (TypeError):
        return "Invalid value"
    return redirect("/")
