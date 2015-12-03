from bs4 import BeautifulSoup
from ConfigParser import SafeConfigParser
import requests
import sys, json
import urllib2
import os

#url = raw_input("Enter a website to extract the URL's from: ")

#<TV SHOW> <S01E02>

def download(magnet):
    global IP, USER, PASS

    cmd = "transmission-remote "
    cmd = cmd + "%s -n %s:%s --add '%s'" % (IP, USER, PASS, magnet)
    #print cmd
    os.system(cmd)

argList = sys.argv
try:
    show = argList[1]
    episode = argList[2]
except:
    print "ERROR <TV SHOW> <S01E01>"
    sys.exit(1)


CONFIG_FILE = "./config.ini"

parser = SafeConfigParser()
parser.read(CONFIG_FILE)

USER = parser.get("config", "username")
PASS = parser.get("config", "password")
IP = parser.get("config", "ip")

url =  urllib2.quote('kat.cr/usearch/'+show.lower()+' '+episode.lower()+' hdtv x264/')



headers = {
        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.117 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.8'
        'Accept-Encoding: gzip, deflate',
        'Referer': 'http://google.com',
        'Connection': 'keep-alive',
        }
        
#print url

stringURL = "https://" + url

#print stringURL

r  = requests.get(stringURL,headers=headers, verify=False)
 
data = r.text

soup = BeautifulSoup(data)
 

titles = soup.findAll('a', attrs = { 'title' : 'Torrent magnet link' })

for title in titles:
	magnet = title.get('href')
	#print magnet
	break
	
#print magnet
download(magnet)


#d  = requests.get(magnet)
#print d.text

