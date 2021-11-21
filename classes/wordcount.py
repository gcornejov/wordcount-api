class WordCount():
	def __init__(self, text):
		self.text = text

	def wordcount(text):
		counts = dict()
		words = text.split()

		for word in words:
			if word in counts:
				counts[word] += 1
			else:
				counts[word] = 1

		return counts
