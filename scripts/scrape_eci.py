#!/usr/bin/env python
import os
import sys
from bs4 import BeautifulSoup

import requests

def test(url):
    data_new = requests.get(url).content
    soup = BeautifulSoup(data_new, 'html.parser')
    table_data = soup.find_all('table')
    list_temp = []
    for data_raw in table_data:
        print (len(data_raw))
        try:
            if data_raw['style'].find('font-weight:lighter') != -1:
                list_temp.append(data_raw)
        except:
            pass

    data_1 = list_temp[0].find_all('tr')
    del data_1[0:4]
    for da_te in data_1:
        temp_list = []
        td_data = da_te.find_all('td')
        for temp in td_data:
            temp_list.append(temp.text)
        data_fetch.append(temp_list)
    return

data_fetch = []
data_headers = []
data_remaining_urls = []
data_url = 'http://eciresults.nic.in/'
csv_url = data_url + 'statewiseS19.htm?st=S19'
data = requests.get(csv_url).content
soup = BeautifulSoup(data, 'html.parser')
table_data = soup.find_all('table')
list_1 = []
for data_raw in table_data:
    print (len (data_raw))
    try:
        if data_raw['style'].find('font-weight:lighter') != -1:
            list_1.append(data_raw)
    except:
        pass

data_1 = list_1[0].find_all('tr')
del data_1[0:2]
import ipdb;ipdb.set_trace()
data_headers = [temp.text for temp in data_1[0].find_all('th')]
del data_1[0]
remain_urls = data_1[0]
for temp in remain_urls.find_all('a'):
    data_remaining_urls.append(temp['href'])
if(data_remaining_urls[0] == data_remaining_urls[-1]):
    print data_remaining_urls
    del data_remaining_urls[-1]
    print data_remaining_urls

del data_1[0]
for da_te in data_1:
    temp_list = []
    td_data = da_te.find_all('td')
    for temp in td_data:
        temp_list.append(temp.text)
    data_fetch.append(temp_list)

for temp in data_remaining_urls:
    url = data_url+temp
    test(url)
data_fetch.insert(0,data_headers)
import csv
del data_fetch[-1]
with open('test1.csv', 'w') as fp:
    a = csv.writer(fp, delimiter=',')
    a.writerows(data_fetch)
