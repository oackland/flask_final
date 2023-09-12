import datetime

from flask import Flask, render_template, url_for, request

app = Flask(__name__)
tracker = ["Test Habits", "clean Room", "eat Breakfast"]


@app.context_processor
def add_calc_date_range():
	def date_range(start: datetime.date):
		dates = [start + datetime.timedelta(days=diff) for diff in range(-3, 4)]
		return dates

	return {"date_range": date_range}


@app.route("/")
def home():
	date_str = request.args.get("date")
	if date_str:
		selected_date = datetime.date.fromisoformat(date_str)
	else:
		selected_date = datetime.date.today()
	return render_template(
		"index.html", tracker=tracker, title="Home", 	selected_date=selected_date
	)


@app.route("/add", methods=["GET", "POST"])
def add_habit():
	if request.method == "POST":
		tracker.append(request.form.get("habit"))
	return render_template("add_habit.html", title="Tracker", selected_date=datetime.date.today(),
						)



@app.route("/fizzbuzz")
def fizzbuzz():
	return render_template("fizzbuzz.html", title="Fizzbuzz")


if __name__ == "__main__":
	app.run(host='0.0.0.0', port=5001, debug=True)
