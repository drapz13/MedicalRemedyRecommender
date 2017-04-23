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

url1="https://www.icliniq.com/qa/specialities/dermatologist?"+"page="
counter=1
for i in range(1,50):
    url=url1+str(i)
    #print(url)
    s=urllib.request.urlopen(url)
    s=s.read().decode("UTF-8")
    s=s.replace('\n','\n')

    #print(s)
    '''
    begintable = s.find("table")
    endtable = s.find("</table>")
    s=s[begintable:endtable]
    '''

    nameslist=[]

    startname="<a class=\"biglink\" href=\"/qa/"
    endname="style=\"font-size:17px"

    for it in re.finditer(startname,s):
        namelocstart=s.find(startname,it.start())+29
        #namelocstart=s.find("/",it.start())
        namelocend=s.find(endname,it.start())-2
        filename= s[namelocstart:namelocend].replace('-',' ')
        namelocstart1=filename.find("/")
        filename=filename[namelocstart1+1:]
        print(filename)
        print("---------------------------------------------")
        nameslist.append(filename)
        
    for i in nameslist:
        print()
        print("question: ",end="")
        with open("db1.txt", 'a') as out:
            out.write(i + '\n\n')
        print(i)
        counter=counter+1
    #print(s)
