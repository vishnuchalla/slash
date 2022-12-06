from flask import Flask, jsonify, request
from slash import extractProducts, send_email
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/slash/', methods=['GET'])
def slash():
    args = request.args
    ret = extractProducts(args)
    send_email(ret, args)
    return jsonify(ret)


@app.route('/hello/', methods=['GET'])
def welcome():
    return "Hello World!"


if __name__ == '__main__':
    app.run(debug=False)
