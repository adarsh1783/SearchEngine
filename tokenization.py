from util import *

# Add your import statements here

from nltk import word_tokenize


class Tokenization():

	def naive(self, text):
		"""
		Tokenization using a Naive Approach

		Parameters
		----------
		arg1 : list
			A list of strings where each string is a single sentence

		Returns
		-------
		list
			A list of lists where each sub-list is a sequence of tokens
		"""

		tokenizedText = []
		for S in text:
			S = S.lower()
			ltemp = S.split()
			l = []
			for w in ltemp:
				x = check(w)
				if(len(x)):
					l = l+x
				else:
					l.append(w)
			tokenizedText.append(l)

		return tokenizedText

	def pennTreeBank(self, text):
		"""
		Tokenization using the Penn Tree Bank Tokenizer

		Parameters
		----------
		arg1 : list
			A list of strings where each string is a single sentence

		Returns
		-------
		list
			A list of lists where each sub-list is a sequence of tokens
		"""

		tokenizedText = []

		for sentence in text:
			sentence = sentence.lower()
			words = word_tokenize(sentence)
			tokenizedText.append(words)

		return tokenizedText
