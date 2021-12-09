from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html", page_name="Home Page")


@app.route("/cv/")
def cv():
    return render_template("cv.html", page_name="CV")


@app.route("/login/", methods=["GET", "POST"])
def login():
    error = None
    if request.method == "POST":
        if request.form["username"] != "hubert" or request.form["password"] != "dev":
            error = "Invalid Credentials. Please Try Again!"
        else:
            return redirect(url_for("home", username=request.form["username"]))
    return render_template("login.html", page_name="Login", error=error)


@app.errorhandler(Exception)
def handle_not_found(error):
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)
