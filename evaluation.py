from util import *

# Add your import statements here




class Evaluation():

	def queryPrecision(self, query_doc_IDs_ordered, query_id, true_doc_IDs, k):
		"""
		Computation of precision of the Information Retrieval System
		at a given value of k for a single query

		Parameters
		----------
		arg1 : list
			A list of integers denoting the IDs of documents in
			their predicted order of relevance to a query
		arg2 : int
			The ID of the query in question
		arg3 : list
			The list of IDs of documents relevant to the query (ground truth)
		arg4 : int
			The k value

		Returns
		-------
		float
			The precision value as a number between 0 and 1
		"""

		precision = -1

		#Fill in code here
		count = 0
		for i in range(k):
			if query_doc_IDs_ordered[i] in true_doc_IDs:
				count = count + 1
		
		if k and true_doc_IDs:
			precision = count / k
		else:
			precision = 1
			
		return precision


	def meanPrecision(self, doc_IDs_ordered, query_ids, qrels, k):
		"""
		Computation of precision of the Information Retrieval System
		at a given value of k, averaged over all the queries

		Parameters
		----------
		arg1 : list
			A list of lists of integers where the ith sub-list is a list of IDs
			of documents in their predicted order of relevance to the ith query
		arg2 : list
			A list of IDs of the queries for which the documents are ordered
		arg3 : list
			A list of dictionaries containing document-relevance
			judgements - Refer cran_qrels.json for the structure of each
			dictionary
		arg4 : int
			The k value

		Returns
		-------
		float
			The mean precision value as a number between 0 and 1
		"""

		meanPrecision = -1

		#Fill in code here
		Precision = [0 for i in range(len(query_ids))]
		for i in range(len(query_ids)):
			query_doc_IDs_ordered = doc_IDs_ordered[i]
			query_id = query_ids[i]
			true_doc_IDs = [int(qrel["id"]) for qrel in qrels if int(qrel["query_num"]) == query_id]
			
			Precision[i] = self.queryPrecision(query_doc_IDs_ordered,query_id,true_doc_IDs,k)
			
		meanPrecision = sum(Precision) / len(Precision)

		return meanPrecision

	
	def queryRecall(self, query_doc_IDs_ordered, query_id, true_doc_IDs, k):
		"""
		Computation of recall of the Information Retrieval System
		at a given value of k for a single query

		Parameters
		----------
		arg1 : list
			A list of integers denoting the IDs of documents in
			their predicted order of relevance to a query
		arg2 : int
			The ID of the query in question
		arg3 : list
			The list of IDs of documents relevant to the query (ground truth)
		arg4 : int
			The k value

		Returns
		-------
		float
			The recall value as a number between 0 and 1
		"""

		recall = -1

		#Fill in code here
		count = 0
		for i in range(k):
			if query_doc_IDs_ordered[i] in true_doc_IDs:
				count = count + 1
		
		if k and true_doc_IDs:
			recall = count / len(true_doc_IDs)
		else:
			recall = 1
			
		return recall


	def meanRecall(self, doc_IDs_ordered, query_ids, qrels, k):
		"""
		Computation of recall of the Information Retrieval System
		at a given value of k, averaged over all the queries

		Parameters
		----------
		arg1 : list
			A list of lists of integers where the ith sub-list is a list of IDs
			of documents in their predicted order of relevance to the ith query
		arg2 : list
			A list of IDs of the queries for which the documents are ordered
		arg3 : list
			A list of dictionaries containing document-relevance
			judgements - Refer cran_qrels.json for the structure of each
			dictionary
		arg4 : int
			The k value

		Returns
		-------
		float
			The mean recall value as a number between 0 and 1
		"""

		meanRecall = -1

		#Fill in code here
		Recall = [0 for i in range(len(query_ids))]
		for i in range(len(query_ids)):
			query_doc_IDs_ordered = doc_IDs_ordered[i]
			query_id = query_ids[i]
			true_doc_IDs = [int(qrel["id"]) for qrel in qrels if int(qrel["query_num"]) == query_id]
			
			Recall[i] = self.queryRecall(query_doc_IDs_ordered, query_id, true_doc_IDs, k)
			
		meanRecall = sum(Recall) / len(Recall)

		return meanRecall


	def queryFscore(self, query_doc_IDs_ordered, query_id, true_doc_IDs, k):
		"""
		Computation of fscore of the Information Retrieval System
		at a given value of k for a single query

		Parameters
		----------
		arg1 : list
			A list of integers denoting the IDs of documents in
			their predicted order of relevance to a query
		arg2 : int
			The ID of the query in question
		arg3 : list
			The list of IDs of documents relevant to the query (ground truth)
		arg4 : int
			The k value

		Returns
		-------
		float
			The fscore value as a number between 0 and 1
		"""

		fscore = -1

		#Fill in code here
		precision = self.queryPrecision(query_doc_IDs_ordered,query_id,true_doc_IDs,k)
		recall = self.queryRecall(query_doc_IDs_ordered, query_id, true_doc_IDs, k)
		
		if precision or recall:
			fscore = (2 * precision * recall) / (precision + recall)
		else:
			fscore = 0
		
		return fscore


	def meanFscore(self, doc_IDs_ordered, query_ids, qrels, k):
		"""
		Computation of fscore of the Information Retrieval System
		at a given value of k, averaged over all the queries

		Parameters
		----------
		arg1 : list
			A list of lists of integers where the ith sub-list is a list of IDs
			of documents in their predicted order of relevance to the ith query
		arg2 : list
			A list of IDs of the queries for which the documents are ordered
		arg3 : list
			A list of dictionaries containing document-relevance
			judgements - Refer cran_qrels.json for the structure of each
			dictionary
		arg4 : int
			The k value
		
		Returns
		-------
		float
			The mean fscore value as a number between 0 and 1
		"""

		meanFscore = -1

		#Fill in code here
		Fscore = [0 for i in range(len(query_ids))]
		for i in range(len(query_ids)):
			query_doc_IDs_ordered = doc_IDs_ordered[i]
			query_id = query_ids[i]
			true_doc_IDs = [int(qrel["id"]) for qrel in qrels if int(qrel["query_num"]) == query_id]
			
			Fscore[i] = self.queryFscore(query_doc_IDs_ordered, query_id, true_doc_IDs, k)
			
		meanFscore = sum(Fscore) / len(Fscore)

		return meanFscore
	

	def queryNDCG(self, query_doc_IDs_ordered, query_id, true_doc_IDs, k):
		"""
		Computation of nDCG of the Information Retrieval System
		at given value of k for a single query

		Parameters
		----------
		arg1 : list
			A list of integers denoting the IDs of documents in
			their predicted order of relevance to a query
		arg2 : int
			The ID of the query in question
		arg3 : list
			The list of IDs of documents relevant to the query (ground truth)
		arg4 : int
			The k value

		Returns
		-------
		float
			The nDCG value as a number between 0 and 1
		"""

		nDCG = -1
		
		#Fill in code here
		DCG = 0
		tmp = [0 for i in range(k)]
		for i in range(k):
			if query_doc_IDs_ordered[i] in true_doc_IDs:
				rel = true_doc_IDs[query_doc_IDs_ordered[i]];
				DCG = DCG + (pow(2,rel)-1)/ np.log2(i+2)
				tmp[i] = rel
				
		tmp.sort(reverse = True)
		
		IDCG = 0
		for i in range(k):
			if tmp[i]:
				IDCG = IDCG + (pow(2,tmp[i])-1) / np.log2(i+2)
		
		if IDCG:
			nDCG = DCG / IDCG
		else:
			nDCG = 0
		
		return nDCG


	def meanNDCG(self, doc_IDs_ordered, query_ids, qrels, k):
		"""
		Computation of nDCG of the Information Retrieval System
		at a given value of k, averaged over all the queries

		Parameters
		----------
		arg1 : list
			A list of lists of integers where the ith sub-list is a list of IDs
			of documents in their predicted order of relevance to the ith query
		arg2 : list
			A list of IDs of the queries for which the documents are ordered
		arg3 : list
			A list of dictionaries containing document-relevance
			judgements - Refer cran_qrels.json for the structure of each
			dictionary
		arg4 : int
			The k value

		Returns
		-------
		float
			The mean nDCG value as a number between 0 and 1
		"""

		meanNDCG = -1

		#Fill in code here
		NDCG = [0 for i in range(len(query_ids))]
		for i in range(len(query_ids)):
			query_doc_IDs_ordered = doc_IDs_ordered[i]
			query_id = query_ids[i]
			true_doc_IDs={int(qrel["id"]):5-int(qrel["position"]) for qrel in qrels if int(qrel["query_num"]) == query_id}
			
			NDCG[i] = self.queryNDCG(query_doc_IDs_ordered, query_id, true_doc_IDs, k)
			
		meanNDCG = sum(NDCG) / len(NDCG)

		return meanNDCG


	def queryAveragePrecision(self, query_doc_IDs_ordered, query_id, true_doc_IDs, k):
		"""
		Computation of average precision of the Information Retrieval System
		at a given value of k for a single query (the average of precision@i
		values for i such that the ith document is truly relevant)

		Parameters
		----------
		arg1 : list
			A list of integers denoting the IDs of documents in
			their predicted order of relevance to a query
		arg2 : int
			The ID of the query in question
		arg3 : list
			The list of documents relevant to the query (ground truth)
		arg4 : int
			The k value

		Returns
		-------
		float
			The average precision value as a number between 0 and 1
		"""

		avgPrecision = -1

		#Fill in code here
		count = 0
		total = 0
		avgPrecision = 0
		for i in range(k):
			total = total + 1
			if query_doc_IDs_ordered[i] in true_doc_IDs:
				count = count + 1
				avgPrecision = avgPrecision + count / total
				
		if count:
			avgPrecision = avgPrecision / count
			
		return avgPrecision


	def meanAveragePrecision(self, doc_IDs_ordered, query_ids, qrels, k):
		"""
		Computation of MAP of the Information Retrieval System
		at given value of k, averaged over all the queries

		Parameters
		----------
		arg1 : list
			A list of lists of integers where the ith sub-list is a list of IDs
			of documents in their predicted order of relevance to the ith query
		arg2 : list
			A list of IDs of the queries
		arg3 : list
			A list of dictionaries containing document-relevance
			judgements - Refer cran_qrels.json for the structure of each
			dictionary
		arg4 : int
			The k value

		Returns
		-------
		float
			The MAP value as a number between 0 and 1
		"""

		meanAveragePrecision = -1

		#Fill in code here
		AveragePrecision = [0 for i in range(len(query_ids))]
		for i in range(len(query_ids)):
			query_doc_IDs_ordered = doc_IDs_ordered[i]
			query_id = query_ids[i]
			true_doc_IDs = [int(qrel["id"]) for qrel in qrels if int(qrel["query_num"]) == query_id]
			
			AveragePrecision[i] = self.queryAveragePrecision(query_doc_IDs_ordered, query_id, true_doc_IDs, k)
			
		meanAveragePrecision = sum(AveragePrecision) / len(AveragePrecision)

		return meanAveragePrecision

