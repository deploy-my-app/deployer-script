"""
This script is the main point of the script with all restfull controlls
"""

from flask import Flask

app = Flask(__name__)

from server.routes import *

if __name__ == "__main__":
    app.run()
