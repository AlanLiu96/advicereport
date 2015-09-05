from flask import Flask, Response, request, jsonify, json

app = Flask(__name__, static_folder='static')

@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    app.run(debug = True)