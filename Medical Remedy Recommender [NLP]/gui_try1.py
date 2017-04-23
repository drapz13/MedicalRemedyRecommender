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
from tkinter import *
fields = 'Query',

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

def fetch(entries):
   for entry in entries:
      field = entry[0]
      text  = entry[1].get()
      print('%s: "%s"' % (field, text)) 

def makeform(root, fields):
   entries = []
   for field in fields:
      row = Frame(root)
      lab = Label(row, width=15, text=field, anchor='w')
      ent = Entry(row)
      row.pack(side=TOP, fill=X, padx=5, pady=5)
      lab.pack(side=LEFT)
      ent.pack(side=LEFT, expand=YES, fill=X)
      entries.append((field, ent))
   return entries

def showq(ents):
	user_query=str(fetch(ents))
	with open("db1.txt", 'r') as ques:
   		quests=ques.readlines()
	questions=[x.strip('\n') for x in quests]
	while '' in questions:
		questions.remove('')

	simi=-1
	matched_ques=[]
	for strr1 in questions:
		xx1=lemmatized_string(strr1)
		xx2=lemmatized_string(user_query)
		simi1=jaccard_similarity(xx1,xx2)
		if(simi1>0.20):
			matched_ques.append((simi1,strr1))
		# if(simi1>simi):
		# 	simi=simi1
		# 	matched_ques=strr1


	tfidf_vectorizer = TfidfVectorizer()
	query1=(" ").join(x for x in lemmatized_string(user_query))

	documents=[]
	documents.append(query1)

	for i in questions:
		i1=(" ").join(x for x in lemmatized_string(i))
		documents.append(i1)
	documents=tuple(documents)
	tfidf_matrix = tfidf_vectorizer.fit_transform(documents)
	cos_sim=cosine_similarity(tfidf_matrix[0:1], tfidf_matrix)

	xxx=[]
	xxx.append((user_query,1.0))
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
	
	listbox = Listbox(Tk())
	listbox.pack()

	ht=len(xxx)-1
	for item in xxx[1:]:
		listbox.insert(END, item[0])



# if __name__ == '__main__':
lemmatizer = WordNetLemmatizer()



root = Tk()
root.title('Medical Remedy Recommender')
Label(text='What is the problem you are suffering from ?').pack(side=TOP,padx=10,pady=10)

entry = Entry(root, width=30, height=20)
entry.pack(side=TOP,padx=1,pady=1)

def onok():
    user_query= entry.get()
    

Button(root, text='OK', command=onok).pack(side=LEFT, padx=5,pady=5)
Button(root, text='CLOSE').pack(side= RIGHT)

root.mainloop()




root = Tk()
ents = makeform(root, fields)

b1 = Button(root, text='Show', command=lambda : showq(ents))
b1.pack(side=LEFT, padx=5, pady=5)

b2 = Button(root, text='Quit', command=root.quit)
b2.pack(side=LEFT, padx=5, pady=5)

root.mainloop()	