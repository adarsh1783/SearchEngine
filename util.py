# Add your import statements here
import scipy as np

# Add any utility functions here
def check(word):
	x = len(word)
	l = []
	if(x>2):
		if(word[x-2] == "'"):
			if(word[x-3] == 'n'):			#consider all words ending with n't
				l.append(word[:x-3])
				l.append(word[x-3:])
			else:							#consider all other words which has ' at second last position ex: i'd
				l.append(word[:x-2])
				l.append(word[x-2:])
		elif(word[x-3] == "'"):				#ex: he'll, we'll
			l.append(word[:x-3])
			l.append(word[x-3:])
		if(word[0]>='!' and word[0]<'/'):
			l.append(word[0])
			if(word[x-1]>='!' and word[x-1]<'/'):  #ex: (hello) -> splits into ( , hello & )
				l.append(word[1:x-1])
				l.append(word[x-1:])
			else:							#ex: (hello splits into ( & hello
				l.append(word[1:])
		elif(word[x-1]>='!' and word[x-1]<'/'):   #ex: hello! splits into hello & !
			l.append(word[:x-1])
			l.append(word[x-1:])

	return l
