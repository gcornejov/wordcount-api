from flask import Flask, request, jsonify
from wordcount import wordcount

app = Flask(__name__)

@app.route('/wordcount', methods=['POST'])
def wordcountRoute():
	text = request.files['file'].read().decode("utf-8")
	counts = wordcount(text)
	print(counts)
	return jsonify(counts)

if __name__ == '__main__':
	app.run(debug=True, port=5000)
