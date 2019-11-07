from flask import Flask, jsonify

from koii import Koii


app = Flask(__name__)


@app.route("/")
def home():
    return jsonify({"status": "success"})


@app.route("/proton", methods=["GET", "PATCH"])
def proton():
    return jsonify({"status": "success", "route": "proton"})


Koii(app)

if __name__ == "__main__":
    app.run(debug=True)
