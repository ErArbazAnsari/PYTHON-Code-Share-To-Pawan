# from nltk.stem import PorterStemmer

# porter = PorterStemmer()
# word = ['running', 'runs', 'ran', 'runner']

# stemmed_Word = [porter.stem(word) for word in word]
# print(stemmed_Word)

# import nltk
# from nltk.corpus import stopwords
# from nltk.tokenize import word_tokenize
# text = "the python programming is very good language for data science"

# tokens = word_tokenize(text)

# #removing stop word
# stop_words = set(stopwords.words('english'))
# filtered_word = [word for word in tokens if word.lower() not in stop_words] 
# print(filtered_word)

# import  numpy as np

# myArray = np.ones((2,5))
# print(myArray)
# print(myArray.shape)


import matplotlib.pyplot as plt
import numpy as np

x = ['cse1', 'cse2', 'cse3']
y = [1,2,3]
plt.bar(x,y)
plt.savefig('./picture.png')
plt.show()

newnp = np.random.randint(0,10)

print(newnp)
print(np.sqrt(newnp))
