# -*- coding: utf-8 -*-
"""
Created on Tue Apr  4 19:11:57 2017

@author: vijay
"""
import os
import requests
from bs4 import BeautifulSoup
import re
import time

url = "https://www.oanda.com/currency/average?amount=1&start_month=3&start_year=2017&end_month=3&end_year=2017&base=USD&avg_type=Month&Submit=1&exchange=ARS&exchange=BOB&exchange=CLP&exchange=COP&exchange=CRC&exchange=DOP&exchange=EUR&exchange=GTQ&exchange=HNL&exchange=MXN&exchange=PEN&exchange=SEK&exchange=USD&exchange=VEF&interbank=0&format=CSV"
page=requests.get(url)
soup=BeautifulSoup(page.content,'html.parser')

rates=soup.find(id='menu_content').find_all('pre')

f=open('currency_bs4_1.csv','w')

for i in range(1,15):
    t=re.sub(r'\n(.*)\n(.)',r'\1,\2',rates[i].text)
    print(t)
    f.write(t)
f.close()    

os.startfile('currency_bs4_1.csv')
