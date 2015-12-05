#
from TVShowClass import TVClass
from DBService import Service
from bs4 import BeautifulSoup
from ConfigParser import SafeConfigParser
import requests
import sys, json
import urllib2
import os

def download(magnet, season, episode, show):
    global IP, USER, PASS

    cmd = "transmission-remote "
    cmd = cmd + "%s -n %s:%s --add '%s'" % (IP, USER, PASS, magnet)
    #print cmd
    os.system(cmd)
    
    updateEpisode  = episode + 1
    service1 = Service()
    service1.updateShow(show, season, updateEpisode)
    
def getSQL():
	
	tvArray = [TVClass]
	service = Service()
	tvArray = service.returnShows()
	return tvArray

def showRequest(show, series, season, episode):

	url =  urllib2.quote('kickassunblock.net/usearch/'+show.lower()+' '+series.lower()+' hdtv ettv x264/')


	headers = {
        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.117 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.8'
        'Accept-Encoding: gzip, deflate',
        'Referer': 'http://google.com',
        'Connection': 'keep-alive',
        }
        

	stringURL = "http://" + url

	r  = requests.get(stringURL,headers=headers, verify=False)
 
	data = r.text

	soup = BeautifulSoup(data)

	titles = soup.findAll('a', attrs = { 'title' : 'Torrent magnet link' })

	tvMagnet = None

	for title in titles:
		tvMagnet = title.get('href')
		break
	
	download(tvMagnet, season, episode, show)
	
	
	
"""
    Class starts
"""	
CONFIG_FILE = "./config.ini"

parser = SafeConfigParser()
parser.read(CONFIG_FILE)

USER = parser.get("config", "username")
PASS = parser.get("config", "password")
IP = parser.get("config", "ip")



allTVShows = [TVClass]
alTVShows = getSQL()

for show in alTVShows:
	
	print show.season
	
	episode = None
	season = None
	
	if show.season < 10:
		season = "S0%d" %show.season
	else: 
		season = "S%d" %show.season
		
	if show.episode < 10:
		episode = "E0%d" %show.episode
	else:
		episode = "E%d" %show.episode
		
	serie = season+episode
	print serie
	showRequest(show.name, serie, show.season, show.episode)
	
else:
	print("Database Empty")


# argList = sys.argv
# try:
#     show = argList[1]
#     episode = argList[2]
# except:
#     print "ERROR <TV SHOW> <S01E01>"
#     sys.exit(1)



