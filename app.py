from flask import Flask, render_template, request, redirect, url_for, session, flash
from datetime import datetime
import os

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY", "change-this-in-production")

DEMO_USER = {"email": "demo@arbitrace.app", "password": "demo123", "name": "Demo Investor"}

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login", methods=["GET","POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email","").strip()
        password = request.form.get("password","")
        if email == DEMO_USER["email"] and password == DEMO_USER["password"]:
            session["user"] = {"email": email, "name": DEMO_USER["name"]}
            return redirect(url_for("dashboard"))
        flash("Login demo: demo@arbitrace.app / demo123")
    return render_template("login.html")

@app.route("/register", methods=["GET","POST"])
def register():
    if request.method == "POST":
        flash("Mode demo: registrasi siap dihubungkan ke Supabase Auth.")
        return redirect(url_for("login"))
    return render_template("register.html")

@app.route("/dashboard")
def dashboard():
    if "user" not in session:
        return redirect(url_for("login"))
    stats = {
        "portfolio": 1422.95, "deposit": 1125.00, "investment": 200.00,
        "profit": 97.95, "withdraw": 0.00, "referrals": 3
    }
    return render_template("dashboard.html", user=session["user"], stats=stats)

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
