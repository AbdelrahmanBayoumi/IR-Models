from flask import Flask

app = Flask(__name__)

from statistical_model import routes
