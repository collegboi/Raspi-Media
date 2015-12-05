#!/usr/bin/python

from TVShowClass import TVClass
import sqlite3

class DBAO(object):
	
	conn = None
	
	def __init__(self):
		self.conn = sqlite3.connect('tvShows.db')

	def createDB(self):
		self.conn.execute('''CREATE TABLE IF NOT EXISTS SHOW
		   (ID INTEGER PRIMARY KEY  AUTOINCREMENT,
		   NAME           TEXT    NOT NULL,
		   SEASON         INTEGER     NOT NULL,
		   EPISODE       INTEGER	NOT NULL,
		   AVAIL      INTEGER DEFAULT 0);''')
		
	def insertDB(self, showName, season, episode):
		print("DB Inserting..")
		try:
			self.conn.execute("INSERT INTO SHOW (NAME , SEASON , EPISODE , AVAIL) VALUES ( ? , ?, ?, 1 )", ( showName, season, episode))
			self.conn.commit()
			return "Succesfully Added"
		except sqlite3.OperationalError, msg:
			return "Error in Adding"
		
	def updateDB(self, name, season, episode):
		print("DB Updating...")
		try:
			self.conn.execute("UPDATE TABLE SHOW SET SEASON =? && EPISODE =? WHERE NAME =?", (season, episode, name) )
			self.conn.commit()
			return "Succesfully Update"
		except sqlite3.OperationalError, msg:
			return "Error in Update"
	
	def updateDBAvail(self, showname, avail):
		print("DB Avail updating....")
		try:
			self.conn.execute("UPDATE SHOW SET AVAIL =? WHERE NAME =?", (avail, showname) )
			self.conn.commit()
			return "Succesfully Update"
		except sqlite3.OperationalError, msg:
			return "Error in Update"
	
	def selectDB(self):
		objectList = []
		#print("DB Selecting...")
		cursor = self.conn.execute("SELECT id, name, season, episode, avail  from SHOW")
		for row in cursor:
			if row[4] == 1:
				show = TVClass(row[1], row[2], row[3], row[4])
				objectList.append(show)
		return objectList
			
	def closeDB(self):
		self.conn.close()