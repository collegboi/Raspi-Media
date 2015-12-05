#!/usr/local/bin/python

from DAO import DBAO
import json
# dbao = DBAO()
# dbao.createDB()
# #dbao.insertDB("ARROW",2,1)
# #
# arrayTV = dbao.selectDB()
# dbao.closeDB()

class Service(object):
	
	dbao = None
	#arrayTV = []

	def __init__(self):
		self.dbao = DBAO()
		self.dbao.createDB()
		
	def addNewShow(self, name, season, episode):
		return self.dbao.insertDB(name, season, episode)

	def updateShow(self,name, season, episode):
		return self.dbao.updateDB(name, season, episode)
		
	def haltShow(self, name):
		return self.dbao.updateDBAvail(name,0)
	
	def continueShow(self, name):
		return self.dbao.updateDBAvail(name, 1)
	
	def close(self):
		self.dbao.close()
		
	def getAllShows(self):
		
		response = []
		
		for item in self.dbao.selectDB():
			response.append({'Name': item.getName(), 'Season' : item.getSeason(), 'Episode' : item.getEpisode(), 'Avail':item.getAvail() })
						
		return json.dumps(response)
		
		
	def returnShows(self):
		return self.dbao.selectDB();