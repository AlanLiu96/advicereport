from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/feed')
def feed():
	return feeds1.txt

if __name__ == '__main__':
    app.run()