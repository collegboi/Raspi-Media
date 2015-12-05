
from flask import Flask
from DBService import Service
from TVShowClass import TVClass
import sys, json
import json
import inspect

argList = sys.argv
try:
    name = argList[1]
    season = argList[2]
    episode = argList[3]
    avail = argList[4]
    action = argList[5]
except:
    print "ERROR <tv name> <season> <epsisde> <avail>"
    sys.exit(1)
  
  
if action == "add":
	dbService = Service()
  	print dbService.addNewShow(name, season, episode)

elif action == "show":
  	dbService = Service()
  	print dbService.getAllShows()

elif action == "continue":
  	dbService = Service()
  	print dbService.continueShow(name)

elif action == "halt":
	dbService = Service()
  	print dbService.haltShow(name)

