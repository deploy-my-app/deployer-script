"""
This script is the main point of the script with all restfull controlls
"""

from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    app.run()
