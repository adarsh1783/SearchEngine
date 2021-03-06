from util import *
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer


class InflectionReduction:

	def reduce(self, text):
		"""
		Stemming/Lemmatization

		Parameters
		----------
		arg1 : list
			A list of lists where each sub-list a sequence of tokens
			representing a sentence

		Returns
		-------
		list
			A list of lists where each sub-list is a sequence of
			stemmed/lemmatized tokens representing a sentence
		"""

		reducedText = []
		porter = PorterStemmer()
		wordnet = WordNetLemmatizer()
		for S in text:
			l = []
			for w in S:
				l.append(wordnet.lemmatize(w))
			reducedText.append(l)
		return reducedText


