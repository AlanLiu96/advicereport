from flask import Flask, render
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/feed')
def feed():
	return render_template('feeds1.xml')

if __name__ == '__main__':
    app.run()