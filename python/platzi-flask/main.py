#!/usr/bin/env python3

from flask import Flask, request

app = Flask(__name__)


@app.route("/")
def hello():
    user_ip = request.remote_addr
    return "Hello, Flask! Your ip is {}".format(user_ip)


if __name__ == "__main__":
    app.run(debug=True)
