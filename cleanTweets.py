import re

# name of new file we want to write to
new_file = open('politicians/files/clean/warren.txt', 'w')
# open file to read
with open("politicians/files/warren.txt","r") as f:
	for line in f:
		# remove twitter URLs
		noURL = re.sub(r"http\S+", "", line)
		# remove numbers
		noNum = re.sub(r'\d+', "", noURL)

		## Uncomment below to also remove hashtags and mentions
		# noHashtag = re.sub(r'(\s)#\w+', r'\1', noNum)
		# noTags = re.sub(r'(\s)@\w+', r'\1', noHashtag)
		# clean = re.sub(r'(\s).@\w+', r'\1', noTags)

		# return new text in all lowercase letters
		new_file.write(noNum.lower())

new_file.close()   
