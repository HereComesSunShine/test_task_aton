from flask import Flask, render_template, redirect, request, url_for, session
import sqlite3

app = Flask(__name__)
app.secret_key = "120272"


def get_db_connection():
    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row
    return conn


# from app import views
@app.route("/")
def home_page():
    return render_template("home_page.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    error = None
    if request.method == "POST":
        user_login = request.form["login_input"]
        user_password = request.form["password_input"]

        conn = get_db_connection()
        user = conn.execute(
            "SELECT * FROM users WHERE login = ?", (user_login,)
        ).fetchone()
        conn.close()

        if user is None or user_password != user["password"]:
            error = "Invalid login or password. Please try again."
        else:
            session["user_id"] = user["id"]
            session["user_name"] = user["Name"]
            return redirect(url_for("clients"))

    return render_template("login.html", error=error)


@app.route("/clients")
def clients():
    if "user_id" not in session:
        return redirect(url_for("login"))

    conn = get_db_connection()
    user_name = session["user_name"]
    clients = conn.execute(
        "SELECT * FROM clients WHERE manager = ?", (user_name,)
    ).fetchall()
    conn.close()
    
    
    
    return render_template('clients.html', clients=clients, user_name=user_name)

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for('home_page'))

app.run(debug=True)
