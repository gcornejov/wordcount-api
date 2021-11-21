import re 

class WordCount():
	def __init__(self, text):
		self.text = text

	def __call__(self):
		counts = dict()
		words = self.text.split()

		for word in words:
			re_word = re.sub(r'[^\w\s]', '', word)
			if re_word in counts:
				counts[re_word] += 1
			else:
				counts[re_word] = 1

		return counts
