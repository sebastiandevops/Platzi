#!/usr/bin/env python3

from flask import Flask, request, make_response, redirect, render_template
from flask import session, url_for, flash
from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)

app.config["SECRET_KEY"] = "SUPER SECRETO"

todos = ["Buy coffee", "Develop a website", "Publish a project"]


class LoginForm(FlaskForm):
    username = StringField("Username: ", validators=[DataRequired()])
    password = PasswordField("Password: ", validators=[DataRequired()])
    submit = SubmitField("Submit")


@app.errorhandler(404)
def not_found(error):
    return render_template("404.html", error=error)


@app.errorhandler(500)
def server_error(error):
    return render_template("500.html", error=error)


@app.route("/")
def index():
    user_ip = request.remote_addr
    response = make_response(redirect("/hello"))
    session["user_ip"] = user_ip
    return response


@app.route("/hello", methods=["GET", "POST"])
def hello():
    user_ip = session.get("user_ip")
    login_form = LoginForm()
    username = session.get("username")
    context = {
        "user_ip": user_ip,
        "todos": todos,
        "login_form": login_form,
        "username": username,
    }
    # if login_form.validate_on_submit():
    if request.method == 'POST':
        username = login_form.username.data
        session["username"] = username
        flash("Username successfully registered.")

        return redirect(url_for("index"))
    return render_template("hello.html", **context)


if __name__ == "__main__":
    app.run(debug=True)
