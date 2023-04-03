from flask import Flask
from datetime import datetime


app = Flask(__name__)

from controllers import controller

if __name__ == "__main__":
    app.run(debug=True)
