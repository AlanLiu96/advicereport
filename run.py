from flask import Flask, render, Respose
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/feed')
def feed():
	return Response('feeds1.xml',mimetype='text/xml')

if __name__ == '__main__':
    app.run()