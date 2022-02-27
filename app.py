

from flask import Flask, redirect, url_for, render_template, request, session, flash
from flask.helpers import send_from_directory
import os

from datetime import date
import datetime
import json
import base64

app = Flask(__name__)


@app.route("/new-project", methods=['POST', 'GET'])
def hello_world():  # put application's code here
    return render_template("signup.html")


if __name__ == '__main__':
    app.run(debug=True)
