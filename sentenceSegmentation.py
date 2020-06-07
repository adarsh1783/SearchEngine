from util import *

# Add your import statements here
import string
import nltk


class SentenceSegmentation():

	def naive(self, text):
		"""
		Sentence Segmentation using a Naive Approach

		Parameters
		----------
		arg1 : str
			A string (a bunch of sentences)

		Returns
		-------
		list
			A list of strings where each string is a single sentence
		"""

		segmentedText = []

		op = set(['(','{','['])
		cl = set([')','}',']'])
		br = set(['.','?','!'])
		
		end = []
		i = 0
		while i<len(text):
			#if current char is delimeter
			if text[i] in br:
				# if text[i] == '.':
				# 	'''detecting abbreviation'''
				# 	j = i-1
				# 	while j>=0 and text[j].isalpha():
				# 		j = j-1
				# 	j=j+1
					
				# 	k=i+1
				# 	while k<len(text) and text[k] in string.whitespace:
				# 		k = k+1
				# 	if k<len(text) and text[j].isupper() and text[k].isupper():
				# 		i = i+1
				# 		continue 
				l = i
				i = i+1
				
				#Finding begining of next sentences
				while i<len(text) and (not text[i].isalnum()) and not (text[i] in op):
					if text[i] in cl:
						l = i
					i = i+1
				#Handling Alignment of sentences
				w = i
				for j in range(l+1,i):
					if text[j] in string.whitespace:
						w = j
				i = w+1	
				end.append(i)
				i = i-1
			i = i+1
		end.append(len(text))
		
		#Retrieving all the sentences into a list
		start = 0
		for e in end:
			tmp = text[start:e].strip()
			if tmp:
				segmentedText.append(tmp)
			start=e
		return segmentedText


	def punkt(self, text):
		"""
		Sentence Segmentation using the Punkt Tokenizer

		Parameters
		----------
		arg1 : str
			A string (a bunch of sentences)

		Returns
		-------
		list
			A list of strings where each strin is a single sentence
		"""

		segmentedText = nltk.sent_tokenize(text)
		
		return segmentedText

