#!/usr/bin/python

class TVClass(object):
	
	def __init__(self, name, season, episode, avail):
		self.name = name
		self.season = season
		self.episode = episode
		self.avail = avail
		
	def getName(self):
		return self.name
		
	def getSeason(self):
		return self.season
		
	def getEpisode(self):
		return self.episode
		

	def setSeason(self, season):
		self.season = season
		
	def setEpisode(self, episode):
		self.episode = episode
	
	def setAvail(self, avail):
		self.avail = avail
		
	def getAvail(self):
		return self.avail
	