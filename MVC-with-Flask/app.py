# Imports flask into the project
from flask import Flask, jsonify, redirect, url_for, render_template, request

# Creates a flask instance
app = Flask(__name__)

students = [
    {
        "id": 0,
        "title": "Mr.",
        "first_name": "Dev",
        "last_name": "Something",
    },
]


# Used to route traffic to this function
# "/" means home directory
@app.route("/")
def home():
    return render_template("index.html", page_name="Index Page")


# This route will create a new GET route to our link
# accessible at http://127.0.0.1:5000/api/v1/student/data
@app.route("/api/v1/student/data/", methods=["GET"])
def student_data():
    # ETL = Extract Transform Load
    return jsonify(students)  # Transforms data into JSON


@app.route("/welcome/")
def welcome_screen():
    return render_template("welcome.html", page_name="Welcome Page")


# Generic error handling for any error will redirect to welcome page
@app.errorhandler(Exception)
def handle_not_found(error):
    # Redirect, moves the user to a specified webside
    # usr_for takes an argument of the function in the app rather than url
    return redirect(url_for("welcome_screen"))


# Creates a dynamic page using the <username> variable that is provided by the user
@app.route("/login/<username>/")
def welcome_user(username):
    return render_template("greeting.html", page_name="Greeting", user=username)


@app.route("/login/", methods=["GET", "POST"])
def login():
    error = None
    if request.method == "POST":
        # Checks is user and password provided is "admin"
        if request.form["username"] != "admin" or request.form["password"] != "admin":
            # If not shows the error
            error = "Invalid Credentials. Please Try Again!"
        else:
            # Redirects to the welcome user page and passes the username as argument
            return redirect(url_for("welcome_user", username=request.form["username"]))
    return render_template("login.html", page_name="Login", error=error)


# Base html file used to check that it works
@app.route("/base/")
def base():
    return render_template("base.html", page_name="Base")


if __name__ == "__main__":
    # Runs the application
    app.run(debug=True)
