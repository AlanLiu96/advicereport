from flask import Flask, Response, request, jsonify
from bs4 import BeautifulSoup

f = open('static/feeds1.xml')

xml= f.read()



app = Flask(__name__, static_folder='static')

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/feed')
def feed():
	return Response('feeds1.xml',mimetype='text/xml')

if __name__ == '__main__':
    app.run(debug = True)