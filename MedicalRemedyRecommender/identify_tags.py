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

quest_file = open('db.txt', 'r')
questions_list = quest_file.read().split('\n\n')
#print(questions_list)
quest_file.close()
ques_tags=[]

quest_tag_file = open('tagged_quest.txt', 'w')
#print(questions_list)

for it in questions_list:
    #post_fields = {'text_or_url': it, 'output': 'json', 'max': '300'}
    #request = Request(url, urlencode(post_fields).encode())
    #ques_tags.append(json.loads(urlopen(request).read().decode()))
    #print(ques_tags[0])
    text = nltk.word_tokenize(it)
    write_tag = [x for x in nltk.pos_tag(text, tagset="universal") if( x[1]=="VERB" or x[1]=="NOUN" or x[1]=="ADJ" or x[1]=="ADV")]
    quest_tag_file.write(str(nltk.pos_tag(text, tagset="universal")))
    quest_tag_file.write("\n")
quest_tag_file.close()
