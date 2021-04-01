from flask import Flask

app = Flask(__name__)

from vector_space import routes
