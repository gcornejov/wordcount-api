class WordCount():
	def __init__(self, text):
		self.text = text

	def __call__(self):
		counts = dict()
		words = self.text.split()

		for word in words:
			if word in counts:
				counts[word] += 1
			else:
				counts[word] = 1

		return counts
