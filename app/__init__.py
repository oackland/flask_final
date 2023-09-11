from flask import Flask, render_template, url_for, request

app = Flask(__name__)
tracker = ["Test Habits",  "clean Room",  "eat Breakfast"]


@app.route("/")
def home():
    return render_template("index.html", tracker=tracker, title="Home")


@app.route("/add", methods=["GET", "POST"])
def add_habit():
    if request.form == "POST":
        pass
    return render_template("add_habit.html", title="Tracker")


@app.route("/fizzbuzz")
def fizzbuzz():
    return render_template("fizzbuzz.html", title="Fizzbuzz")


if __name__ == "__main__":
    app.run()
