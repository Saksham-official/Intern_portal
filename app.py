from flask import Flask, render_template, request, redirect, url_for
import json

app = Flask(__name__)

def get_data():     #dummy data
    with open("data.json", "r") as f:
        return json.load(f)
    
@app.route('/', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        return redirect(url_for("dashboard"))
    return render_template("login.html")

@app.route('/dashboard')
def dashboard():
    data = get_data()
    return render_template("dashboard.html", data=data)

@app.route('/leaderboard')
def leaderboard():
    data = get_data()
    return render_template("leaderboard.html", leaderboard=data["leaderboard"])

if __name__ == "__main__":
    app.run(debug=True)