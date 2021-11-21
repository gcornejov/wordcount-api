from flask import Flask

app = Flask(__name__)

@app.route('/wordcount', methods=['POST'])
def wordcountRoute():
	return 'recived'

if __name__ == '__main__':
	app.run(debug=True, port=5000)