from util import *
import sys
from nltk.wsd import lesk
import sklearn
from gensim import corpora, models, similarities
from nltk.corpus import wordnet 

class InformationRetrieval():

	def __init__(self,model_type):
		self.type = model_type
		if self.type == "gensim":
			self.lsamodel = None
			self.index = None
			self.docIDs = None
			self.dictionary = None
			self.tfidf = None
		else:
			self.word_index = None
			self.doc_weights = None
			self.term_weights = None
			self.IDF = None
			self.inverted_indexing = None
	def buildIndex(self, docs, docIDs):
		"""
		Builds the document index in terms of the document
		IDs and stores it in the 'index' class variable

		Parameters
		----------
		arg1 : list
			A list of lists of lists where each sub-list is
			a document and each sub-sub-list is a sentence of the document
		arg2 : list
			A list of integers denoting IDs of the documents
		Returns
		-------
		None
		"""
		if self.type == "gensim":
			doc_clean = []
			for doc in docs:
				doc_tmp = []
				for sent in doc:
					sentence = []
					for w in sent:
						if(w.find('-')!=-1):
							lis = w.split('-')
							sentence.append(lis[0])
							sentence.append(lis[1])
						else:
							sentence.append(w)
					doc_tmp += sentence
				doc_clean.append(doc_tmp)
			self.docIDs = docIDs
			self.dictionary = corpora.Dictionary(doc_clean)
			corpus = [self.dictionary.doc2bow(doc) for doc in doc_clean]
			self.tfidf = models.TfidfModel(corpus, smartirs = 'lfc')
			doc_term_matrix = self.tfidf[corpus]
			self.lsamodel = models.LsiModel(doc_term_matrix, id2word = self.dictionary,num_topics=320)  # train model
			self.index = similarities.MatrixSimilarity(self.lsamodel[doc_term_matrix])
		else:
			word_count = 0
			doc_count = len(docIDs)
			self.word_index = dict()
			self.inverted_indexing = dict()
			freq = dict()
			for doc in docs:
				for sent in doc:
					for word in sent:
						word = lesk(sent, word)
						freq[word] = freq.get(word,0) + 1
			for word in freq:
				if freq[word] != 1:
					self.word_index[word] = word_count
					self.inverted_indexing[word_count] = set()
					word_count += 1
					
			tdm = np.array(np.zeros((word_count,doc_count)))
			for i in range(len(docs)):
				for sentence in docs[i]:
					for word in sentence:
						word = lesk(sentence, word)
						index = self.word_index.get(word,-1)
						if index != -1:
							tdm[index,i] += 1
							self.inverted_indexing[index].add(i)
			non_zero = np.count_nonzero(tdm,axis=1)
			non_zero[non_zero == 0] = 1
			self.IDF = np.log2(doc_count / non_zero)
			del non_zero
			tdm = np.multiply(tdm,np.transpose([self.IDF]))
			u,s,v = np.linalg.svd(tdm,full_matrices=False)
			k = min(s.shape[0],800)
			self.term_weights = np.matmul(np.linalg.inv(np.diag(s[:k])),u[:,:k].T)
			self.doc_weights = np.array(np.zeros((doc_count,k+1)))
			self.doc_weights[:,:k] = np.matmul(v.T[:,:k],np.linalg.inv(np.diag(s[:k])))
			self.doc_weights[:,k] = np.linalg.norm(self.doc_weights[:,:k],axis=1)
			
		return

	def rank(self, queries):
		"""
		Rank the documents according to relevance for each query

		Parameters
		----------
		arg1 : list
			A list of lists of lists where each sub-list is a query and
			each sub-sub-list is a sentence of the query
		

		Returns
		-------
		list
			A list of lists of integers where the ith sub-list is a list of IDs
			of documents in their predicted order of relevance to the ith query
		"""

		doc_IDs_ordered = []
		if self.type == "gensim":
			for query in queries:
				doc = []
				for sent in query:
					sentence = []
					for w in sent:
						if(w.find('-')!=-1):
							lis = w.split('-')
							sentence.append(lis[0])
							sentence.append(lis[1])
						else:
							sentence.append(w)
					doc += sentence
				vec_bow = self.dictionary.doc2bow(doc)
				vec_bow = self.tfidf[vec_bow]
				vec_lsi = self.lsamodel[vec_bow]
				sims = self.index[vec_lsi]
				doc_rank = [k for k, v in sorted(zip(self.docIDs,sims), key=lambda item: -item[1])]
				doc_IDs_ordered.append(doc_rank)
		else:
			for query in queries:
				retrieved_doc = set()
				query_tf = np.zeros((len(self.word_index),))
				for sentence in query:
					for word in sentence:
						word = lesk(sentence, word)
						i = self.word_index.get(word,-1)
						if i != -1:
							query_tf[i] = query_tf[i] + 1
							retrieved_doc.update(self.inverted_indexing[i])
				query_weights = np.multiply(self.IDF,query_tf)
				query_tranform = np.matmul(self.term_weights,query_weights)
				cosine_sim = dict.fromkeys(retrieved_doc,-1)
				Q = np.linalg.norm(query_tranform)
				if Q:
					for doc_i in retrieved_doc:
						cosine_sim[doc_i] = np.dot(query_tranform,self.doc_weights[doc_i,:-1]) / (Q * self.doc_weights[doc_i,-1])
				doc_rank = [k for k, v in sorted(cosine_sim.items(), key=lambda x: x[1], reverse=True)]
				doc_IDs_ordered.append(doc_rank)
			
		return doc_IDs_ordered


