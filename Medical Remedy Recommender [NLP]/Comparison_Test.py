#! python3
import time
import ssl
import os
import datetime
import urllib.request
import json
import requests
from bs4 import BeautifulSoup
import re
import numpy as np
from sklearn.metrics import jaccard_similarity_score
import subprocess
from urllib.parse import urlencode
from urllib.request import Request, urlopen
import nltk
from nltk.stem.wordnet import WordNetLemmatizer
from sklearn.metrics.pairwise import cosine_similarity
from nltk.stem.porter import *
from nltk.stem import *
import operator
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def jaccard_similarity(x,y):
 
    intersection_cardinality = len(set.intersection(*[set(x), set(y)]))
    union_cardinality = len(set.union(*[set(x), set(y)]))
    return intersection_cardinality/float(union_cardinality)


def lemmatized_string(s):
	lemmatized_str=[]
	for i in [x for x in nltk.pos_tag(nltk.word_tokenize(s), tagset="universal") if( x[1]=="VERB" or x[1]=="NOUN" or x[1]=="ADJ" or x[1]=="ADV")]:
		lemmatized_str.append(lemmatizer.lemmatize(i[0], pos=i[1][0].lower()))
	lemm_str=np.array(lemmatized_str)
	return lemm_str


str1="Darpan's leg is paining"
str2="Chintan was in pain"
documents=(str1,str2)
text1 = nltk.word_tokenize(str1)
text2 = nltk.word_tokenize(str2)

# stemmer = PorterStemmer()

# stemmed_list=[stemmer.stem(text) for text in text1]
# print(stemmed_list)


write_tag1 = [x for x in nltk.pos_tag(text1, tagset="universal") if( x[1]=="VERB" or x[1]=="NOUN" or x[1]=="ADJ" or x[1]=="ADV")]
write_tag2 = [x for x in nltk.pos_tag(text2, tagset="universal") if( x[1]=="VERB" or x[1]=="NOUN" or x[1]=="ADJ" or x[1]=="ADV")]

print(write_tag1)
print(write_tag2)

lemmatizer = WordNetLemmatizer()
lemmatized1=[]
lemmatized2=[]

# print(lemmatizer.lemmatize("eating",pos="v"))
# print(lemmatizer.lemmatize("ate",pos="v"))


for i in [x for x in nltk.pos_tag(nltk.word_tokenize(str1), tagset="universal") if( x[1]=="VERB" or x[1]=="NOUN" or x[1]=="ADJ" or x[1]=="ADV")]:
	lemmatized1.append(lemmatizer.lemmatize(i[0], pos=i[1][0].lower()))

for i in write_tag2:
	#print(i[0], i[1])
	lemmatized2.append(lemmatizer.lemmatize(i[0], pos=i[1][0].lower()))

# if len(lemmatized1)>len(lemmatized2):
# 	lemmatized2=lemmatized2+np.zeros(len(lemmatized1)-len(lemmatized2))
# elif len(lemmatized1)<len(lemmatized2) :
# 	lemmatized1=lemmatized1+np.zeros(len(lemmatized2)-len(lemmatized1))
a1=np.array(lemmatized1)
a2=np.array(lemmatized2)
print(a1,a2)
# print(jaccard_similarity(a1,a2))

print(jaccard_similarity(lemmatized1,lemmatized2))
#jaccard_similarity_score(lemmatized1, lemmatized2)
# print(cosine_similarity(np.array([1, 0, -1]), np.array([-1,-1, 0])),"bakwas")

with open("db1.txt", 'r') as ques:
	quests=ques.readlines()

questions=[x.strip('\n') for x in quests]
while '' in questions:
	questions.remove('')

query="permanently get rid jock itch"
# print(questions)

simi=-1
matched_ques=[]
for strr1 in questions:
	xx1=lemmatized_string(strr1)
	xx2=lemmatized_string(query)
	simi1=jaccard_similarity(xx1,xx2)
	if(simi1>0.20):
		matched_ques.append((simi1,strr1))
	# if(simi1>simi):
	# 	simi=simi1
	# 	matched_ques=strr1


tfidf_vectorizer = TfidfVectorizer()
query1=(" ").join(x for x in lemmatized_string(query))

documents=[]
documents.append(query1)

for i in questions:
	i1=(" ").join(x for x in lemmatized_string(i))
	documents.append(i1)
documents=tuple(documents)
tfidf_matrix = tfidf_vectorizer.fit_transform(documents)
cos_sim=cosine_similarity(tfidf_matrix[0:1], tfidf_matrix)

xxx=[]
xxx.append((query,1.0))
for x in np.where(cos_sim[0] >=0.4)[0]:
	# print(cos_sim[0][x])
	if int(cos_sim[0][x]) == 1: 
		continue
	xxx.append((questions[x-1],cos_sim[0][x]))
	# print(documents[x])

# print(documents)
# print(questions)


xxx=sorted(xxx,key=operator.itemgetter(1),reverse=True)
# print(xxx)
# print(xxx)
for i in xxx[1:]:
	# print(i)
	print("Question: ",i[0],'?',"\nMatch Percentage : ",round(i[1]*100,2),"%\n")