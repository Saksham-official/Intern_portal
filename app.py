from flask import Flask, render_template, request, redirect, url_for
import json
import os  # Make sure this is imported near the top

app = Flask(__name__)

# Function to fetch dummy data
def get_data():
    with open("data.json", "r") as f:
        return json.load(f)

# Dummy login page
@app.route('/', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        return redirect(url_for("dashboard"))
    return render_template("login.html")

# Dashboard route
@app.route('/dashboard')
def dashboard():
    data = get_data()
    return render_template("dashboard.html", data=data)

# Leaderboard route
@app.route('/leaderboard')
def leaderboard():
    data = get_data()
    return render_template("leaderboard.html", leaderboard=data["leaderboard"])

# Render deployment port setup
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=False, host='0.0.0.0', port=port)
