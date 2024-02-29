# creating variable to store the number of words
number_of_words = 0

f = open("sample.txt", "r")
f = f.read()
words = f.split()
count = len(words)
print("Total no of words in this document:", count)