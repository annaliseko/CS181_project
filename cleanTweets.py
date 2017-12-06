import nltk
from nltk.corpus import stopwords
import re

stopwords = set(stopwords.words('english'))
# added stopwords to nltk list
stopwords.update(("another","rt", "here", 'go', "i've", "it's", "we've", "we'll", "you're",
					"were","your","their","they're","there","aren't","didn't","that's",
					"however","although","except"))
## uncomment to list all stop words
# print(stopwords)

# name of new file we want to write to
new_file = open('text_clean.txt', 'w')
# open file to read
with open("politicians/files/obama.txt","r") as f:
	for line in f:
		# remove twitter URLs
		result = re.sub(r"http\S+", "", line)
		stringTweet = result.split()
		# remove stopwords
		resultwords  = [word for word in stringTweet if word.lower() not in stopwords]
		result = ' '.join(resultwords)
		# return new text in all lowercase letters
		new_file.write(result.lower())

new_file.close()   