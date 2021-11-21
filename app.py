from flask import Flask, request, jsonify
from classes.wordcount import WordCount

app = Flask(__name__)

@app.route('/wordcount', methods=['POST'])
def wordcountRoute():
	wordcount = WordCount(request.files['file'].read().decode("utf-8"))
	return jsonify(wordcount())

if __name__ == '__main__':
	app.run(debug=True, port=5000)
