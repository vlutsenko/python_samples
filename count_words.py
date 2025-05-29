paragraph = paragraph.lower()
paragraph = paragraph.translate(str.maketrans("", "", string.punctuation))

wordList = paragraph.split()
