from flask import Flask, Response
app = Flask(__name__, static_folder='static', static_url_path='')

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/feed')
def feed():
	return Response('feeds1.xml',mimetype='text/xml')

if __name__ == '__main__':
    app.run()