#!/usr/bin/env python3
""""flask application"""
from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
def home() -> str:
    """homepage of our website"""

    return render_template("0-index.html")


if __name__ == "__main__":
    app.run()
