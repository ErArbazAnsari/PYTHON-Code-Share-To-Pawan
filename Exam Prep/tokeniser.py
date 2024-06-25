# import nltk
from nltk.tokenize import word_tokenize

# text = "This is Arbaz Ansari From Gurgaon Basai Road"
# tokenized_data = word_tokenize(text)
# print(tokenized_data)


from nltk import pos_tag

text = "This is Arbaz Ansari From Gurgaon Basai Road"
token = word_tokenize(text)
posttag = pos_tag(token)
print(posttag)
