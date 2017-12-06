from __future__ import print_function 
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import codecs

import nltk

stopset = set(stopwords.words('english'))

writeFile = codecs.open("outputfile", "w", encoding='utf-8')

with codecs.open("politicians/files/obama.txt", "r", encoding='utf-8') as f:
	line = f.read()
	tokens = nltk.word_tokenize(line)
	tokens = [w.lower() for w in tokens if not w in stopset]
	sep = ''
	for token in tokens:
	    print(token, file=writeFile)
	    # print(' '.join(tokens), file=writeFile)