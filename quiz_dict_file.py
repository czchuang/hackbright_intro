#counts how many times a letter appears in a file

def counts_letters(doc):
	with open(doc) as doc:
		my_doc = doc.read().lower()
		letter_counts = {}
		alphabet = "abcdefghijklmnopqrstuvwxyz"
		for character in my_doc:
			if character in alphabet:
				if character not in letter_counts: 
					letter_counts[character] = 1
				elif character in letter_counts: 
					letter_counts[character] += 1
	return letter_counts

print counts_letters("one_fish_two_fish.txt")

#counts how many times each word appears in a file

def counts_words(doc):
	with open(doc) as doc:
		my_doc = doc.read().lower()
		my_doc = my_doc.replace("\n"," ")
		punctuation = ".,!;`~-:;'/?!@3$%^&*"
		word_counts = {}
		no_punctuation = ""
		
		#strips punctuation from text file
		for character in my_doc:
			if character not in punctuation:
				no_punctuation += character

		#splits text file into list
		no_punctuation = no_punctuation.split()

		#counts words in text file
		for word in no_punctuation:
			if word not in word_counts:
				word_counts[word] = 1
			elif word in word_counts:
				word_counts[word] += 1
	return word_counts

print counts_words("one_fish_two_fish.txt")