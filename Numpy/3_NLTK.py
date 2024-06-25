import nltk.corpus
filePath = nltk.data.find('corpora/words/english')
print(filePath)
with open('test.txt', 'w') as file:
    file.write('This is a test happy')

with open('test.txt', 'r') as file:
    print(file.read())