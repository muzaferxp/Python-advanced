from flask import Flask, jsonify
from core import getData

app = Flask(__name__)


@app.route("/")
def index():
    return jsonify({"Data" : getData() })    

if __name__ == "__main__":
    app.run()
