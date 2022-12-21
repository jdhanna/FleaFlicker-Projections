from flask import Flask

app = Flask(__name__)
app.run(host="https://flea-flicker-projections.herokuapp.com/", port =5000)

from app import routes