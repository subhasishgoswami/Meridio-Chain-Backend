from flask import Flask, Blueprint,jsonify
from flask_cors import CORS
import constants as CONST
from waitress import serve
import os

app = Flask(__name__)
cors = CORS(app)


# endpoint to check service status
@app.route("/status")
def check_status():
    return jsonify({CONST.STATUS: CONST.SUCCESS, CONST.DATA: None})


if __name__ == "__main__":  #Local
    app.run(host="localhost", port="3434", debug=True, use_reloader=True)

