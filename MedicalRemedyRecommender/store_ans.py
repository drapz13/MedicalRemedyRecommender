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

head_url="https://www.icliniq.com/qa/"
url1="https://www.icliniq.com/qa/specialities/dermatologist?"+"page="
counter=1
for i in range(42,50):
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
        qlink=s[namelocstart:namelocend]
        qlink=head_url+qlink
        filename= s[namelocstart:namelocend].replace('-',' ')
        namelocstart1=filename.find("/")
        filename=filename[namelocstart1+1:]
        #print(qlink)
        #print("---------------------------------------------")


        ss=urllib.request.urlopen(qlink)
        ss=ss.read().decode("UTF-8")
        ss=ss.replace('\n','\n')

        startans="icliniq.com.</p>"
        endans="https://www.icliniq.com/ask-a-doctor-online/dermatologist"
        startansloc = ss.find(startans)
        print(startansloc)
        ss=ss[startansloc:]
        endansloc = ss.find(endans)
        print(endansloc)
        ans1=ss[:endansloc-9]
        ans2=re.sub("<[^>]+>","",ans1)
        print(ans2)
        nameslist.append(ans2)

    for i in nameslist:
        print()
        print("question: ",end="")
        with open("db2.txt", 'a') as out:
            out.write(i + '\n\n')
        print(i)
        counter=counter+1
     #print(s)
