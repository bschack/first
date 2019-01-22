import datetime
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def name():
	headline = "Hullo"
	while True:
		now = datetime.datetime.now()
		new_year = now.month == 1 and now.day == 1
		hour = now.hour
		minute = now.minute
		second = now.second
		return render_template("page1.html", new_year=new_year, hour=hour, minute=minute, second=second)



@app.route("/bye")
def bye():
	headline = "byebye"
	return render_template("page2.html", headline=headline)
