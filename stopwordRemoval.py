from util import *

from nltk.corpus import stopwords



class StopwordRemoval():

	def fromList(self, text):
		"""
		Sentence Segmentation using the Punkt Tokenizer

		Parameters
		----------
		arg1 : list
			A list of lists where each sub-list is a sequence of tokens
			representing a sentence

		Returns
		-------
		list
			A list of lists where each sub-list is a sequence of tokens
			representing a sentence with stopwords removed
		"""
		punct = [',','.','(',')','/','\\','-','?','i.e',"n't","'s","e.g.","'",'..','./','=','+','-','etc.','etc']
		stop_words = stopwords.words("english")
		stopwordRemovedText = [[t for t in sent if not t in stop_words + punct] for sent in text]

		return stopwordRemovedText




	

