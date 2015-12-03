from bs4 import BeautifulSoup

import requests
import sys, json
#url = raw_input("Enter a website to extract the URL's from: ")

argList = sys.argv
try:
    data = argList[1]
except:
    print "ERROR"
    sys.exit(1)
    
#print data

#data = "05DL11803"

headers = {
        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.117 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.8'
        'Accept-Encoding: gzip, deflate',
        'Referer': 'http://google.com',
        'Connection': 'keep-alive',
        }

#r  = requests.get("http://" +url)
r = requests.get("https://www.motorcheck.ie/free-car-check/"+data+"/",headers=headers)

data = r.text

soup = BeautifulSoup(data)

# for link in soup.find_all('a'):
#     print(link.get('href'))

returnData = ""
details = []

for strong_tag in soup.find_all('strong'):
	details.append(strong_tag.next_sibling)

#print returnData
returnData = details[6] + " "

titles = soup.findAll('td', attrs = { 'class' : 'car_info pt' })
for title in titles:
    #print title.contents
    temp = title.find('h2')
    if temp:
    	returnData += temp.text

print returnData

#print r.text
