from bs4 import BeautifulSoup
from ConfigParser import SafeConfigParser
import requests
import sys, json
import urllib2
import os


def download(magnet):
    global IP, USER, PASS

    cmd = "transmission-remote "
    cmd = cmd + "%s -n %s:%s --add '%s'" % (IP, USER, PASS, magnet)
    #print cmd
    os.system(cmd)


argList = sys.argv
try:
    movie = argList[1]
    year = argList[2]
except:
    print "ERROR <Movie> <Year>"
    sys.exit(1)


CONFIG_FILE = "./config.ini"

parser = SafeConfigParser()
parser.read(CONFIG_FILE)

USER = parser.get("config", "username")
PASS = parser.get("config", "password")
IP = parser.get("config", "ip")


url =  urllib2.quote(movie.lower()+' '+year+' 1080p/')

#https://www.yify-torrent.org/movie/39005/download-ant-man-2015-1080p-mkv-yify-torrent.html

headers = {
        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.117 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.8'
        'Accept-Encoding: gzip, deflate',
        'Referer': 'http://google.com',
        'Connection': 'keep-alive',
        }
        
#print url

stringURL = "https://www.yify-torrent.org/search/" + url

#print stringURL

r  = requests.get(stringURL,headers=headers, verify=False)

 
data = r.text

soup = BeautifulSoup(data)
 

titles = soup.findAll('a', attrs = { 'class' : 'small button orange' })

for title in titles:
	movURL = title.get('href')
	#print(movURL)
	

movieURL = 'https://www.yify-torrent.org/'+movURL

#movieURL = 'https://www.yify-torrent.org/movie/39005/download-ant-man-2015-1080p-mkv-yify-torrent.html'

d  = requests.get(movieURL)

body = d.text

soup = BeautifulSoup(body)

links = soup.findAll('a', attrs = { 'class' : 'large button orange' })

for link in links:
	magnet = link.get('href')
	download(magnet)
	

#os.system('"%s"'%magnet)