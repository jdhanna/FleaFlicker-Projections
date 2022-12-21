from flask import Flask

app = Flask(__name__)
app.run("0.0.0.0", port=8080)

from app import routes