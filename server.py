from flask import Flask, render_template, url_for, request
from main import data_shoes, data_bags, data_bags_women, data_shoes_women
import json


app = Flask(__name__)


@app.route("/", methods=['POST','GET'])
def main_page():
    return render_template("index.html")


@app.route("/search", methods=["POST"])
def search():
    global money
    money = request.form.get("money")
    return render_template("search.html", money=money)


@app.route("/bags", methods=['POST'])
def pm_bags():
    try:
        if not money :
            return render_template("index.html")
        data_bags(money)
        with open("result_data_bags.json") as file:
            data = json.load(file)
        return render_template("bags.html", data = data)
    except ValueError:
        return render_template("index.html")


@app.route("/bags_women", methods=['POST'])
def pm_bags_women():
    try:
        if not money:
            return render_template("index.html")
        data_bags_women(money)
        with open("result_data_bags_women.json") as file:
            data = json.load(file)
        return render_template("bags_women.html", data = data)
    except ValueError:
        return render_template("index.html")


@app.route("/shoes", methods=['POST'])
def pm_shoes():
    try:
        if not money:
            return render_template("index.html")
        data_shoes(money)
        with open("result_data_shoes.json") as file:
            data = json.load(file)
        return render_template("shoes.html", data = data)
    except ValueError:
        return render_template("index.html")


@app.route("/shoes_women", methods=['POST'])
def pm_shoes_women():
    try:
        if not money:
            return render_template("index.html")
        data_shoes_women(money)
        with open("result_data_shoes_women.json") as file:
            data = json.load(file)
        return render_template("shoes_women.html", data = data)
    except ValueError:
        return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contacts")
def contacts():
    return render_template("contacts.html")


if __name__ == "__main__":
    app.run(debug=True)
