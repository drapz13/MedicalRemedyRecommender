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
import subprocess
from urllib.parse import urlencode
from urllib.request import Request, urlopen
import nltk

#url = "http://termextract.fivefilters.org/extract.php"
#start_tag = "<textarea id=\"text_or_url\" name=\"text_or_url\" rows=\"7\" class=\"dim span6\">"
#print(len(start_tag))
#end_tag = "<\/textarea>"
#quest = "My urologist and dermatologist are saying that I have balanitis. I was given different creams, but the red sports appear again once I stop applying the cream. Coconut oil also seems like working. Is balanitis treatable? I am a known type 2 diabetic, and my current fasting blood sugar is 113 to 125. One month back, when I did not have medicine, it was 165, and my HbA1c was 7.7. I have done HSV 1 and 2 tests thrice, and they were negative. I am observing some mild allergy in my fingers, knees and eyes. I have a few medicines for chest rib hit injury. I am on Glycomet 1 g twice daily."

#text = nltk.word_tokenize(quest)

#tags = nltk.pos_tag(text, tagset="universal")
#useful_tags = [x for x in tags if ( x[1]=="NOUN" or x[1]=="ADJ" or x[1]=="ADV" or x[1]=="VERB")]

#print(useful_tags)
#print(help(nltk.pos_tag_sents))

quest_file = open('db.txt', 'r')
questions_list = quest_file.read().split('\n\n')
#print(questions_list)
quest_file.close()
ques_tags=[]
'''
for it in questions_list:
    post_fields = {'text_or_url': it, 'output': 'json', 'max': '300'}
    request = Request(url, urlencode(post_fields).encode())
    ques_tags.append(json.loads(urlopen(request).read().decode()))
    #print(ques_tags[0])
'''

db_q_tags=nltk.pos_tag_sents(questions_list)

print(db_q_tags)
