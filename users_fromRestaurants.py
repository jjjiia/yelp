#!/usr/bin/env python

import urllib2
import sys
import json
from bs4 import BeautifulSoup, NavigableString
import re
import csv
import datetime
import os
import time
import random

# download user, review or stars?, location, date, number of reviews by same user
# clean and put in array for each
# save to flat file
soupfile = open("cambridge_soup3.csv","a+")
soupwriter = csv.writer(soupfile)
userfile = open("cambridge_users2.csv", "a+")
userwriter = csv.writer(userfile)

reviewStatsfile = open("cambridge_reviewStats2.csv", "a+")
reviewStatswriter = csv.writer(reviewStatsfile)

finishedLinks = open("finishedLinks.csv", "a+")
finishedLinksWriter = csv.writer(finishedLinks)

def download_craigslist():
	page_count = 100
	i = 0
	links = buildLinksArray()
	#links = ["big-bite-restaurant-and-bbq-somerville","montecristo-mexican-grill-boston"]
	for link in links:
		formatedLink = str(link)[2:-2]
		#formatedLink = str(link)

		for i in range(page_count):
			#print i
			pageNumber = int(i)*40
			#print pageNumber
			url= "http://www.yelp.com/biz/"+formatedLink+"?start="+str(pageNumber)
			print url
			soup = BeautifulSoup(urllib2.urlopen(url).read())
			time.sleep(random.random()*10)
			
			soupwriter.writerow(str(soup))
			location =  soup.find_all("li",{"class":"user-location"})
			location = re.sub("<.*?>"," ",str(location))
			location = re.sub(r"[\xc2\xa0\xe2\x80\x99]","",location)
			cleanLocation = " ".join(location.split())
			
			users = soup.find_all("a",{"class":"user-display-name"})
			users = str(users).split(",")
			for user in users:
				#cleanUser = re.sub("<.*?>"," ",str(user))
				cleanUser = re.sub(r"[\xc2\xa0\xe2\x80\x99]","",user)
				userwriter.writerow(cleanUser)
				
			date = soup.find_all("span",{"class":"rating-qualifier"})
			date = re.sub("<.*?>"," ",str(date))
			date = re.sub(r"[\xc2\xa0\xe2\x80\x99]","",date)
			cleanDate = " ".join(date.split())
			
			userStats = soup.find_all("ul",{"class":"user-passport-stats"})
			cleanUserStats = re.sub("<.*?>"," ",str(userStats))
			cleanUserStats = re.sub(r"[\xc2\xa0\xe2\x80\x99]","",cleanUserStats)
			cleanUserStats = " ".join(cleanUserStats.split())
			
			#print cleanUser
			print link, cleanUserStats, cleanDate, cleanLocation
			reviewStatswriter.writerow([link, cleanUserStats, cleanDate, cleanLocation])
			print len(cleanUserStats)
			if len(cleanUserStats) < 5:
				finishedLinksWriter.writerow(url)
				time.sleep(random.random()*10)
				break
	        #i = i+1
        #print url        #link = 'http://'+basecity+baseURL1 +city+baseURL2 + str(i+1)
        #print link
#        soup = BeautifulSoup(urllib2.urlopen(url).read())
#        #x =  soup.body.article.section.div
#        location =  soup.find_all("li",{"class":"user-location"})
#        user = soup.find_all("li",{"class":"user-name"})
#        date = soup.find_all("span",{"class":"rating-qualifier"})
#        locationwriter.writerow([restaurant, location])
#        userwriter.writerow([restaurant, user])
#        datewriter.writerow([restaurant, date])
		
        #print date, user, location
        #spamwriter.writerow([restaurant,date, user, location])
        #j=0
        #print [len(date), len(user), len(location)]
        #for j in range(len(user)):
		#	entry = [date[j], user[j], location[j]]
		#	#print entry
		#	#entries.append(entry)
		#	spamwriter.writerow([restaurant,entry])
#		#	
       # for tag in entries:
       #     #linkOnly = str(tag).split("\"")[2]
       #     #print tag.split("\"")[1]
       #     linkOnly = re.sub("<.*?>", " ", str(tag))
       #     test = re.sub(r"[\xc2\xa0\xe2\x80\x99]","",linkOnly)
       #     test =" ".join(test.split())
       #     test =  test.strip()                
       #     locationDict[test] = locationDict.get(test,0)+1
       #     print test
       #     #spamwriter.writerow(test)
            #link = tag.find_all('a')
            #print link
        	#	art.append(ah['href'])

def cleanLinks():
	inputfile = open("data/cambridge_restaurantLinks.csv","r")
	spamreader = csv.reader(inputfile)
	for row in spamreader:
		if "adredir" not in str(row):
			print row
	
def buildLinksArray():
	linksArray = []
	inputfile = open("boston_combinedLinks.csv","r")
	spamreader = csv.reader(inputfile)
	for row in spamreader:
			if row not in linksArray:
				linksArray.append(row)
	return linksArray
print buildLinksArray()


def buildAlreadyFinishedArray():
	noduplinksArray = []
	inputfile = open("finishedLinks.csv","r")
	currentLinks = buildLinksArray()
	spamreader = csv.reader(inputfile)
	for finishedlink in spamreader:
		for link in currentLinks:
			if link in finishedlink:
				print "duplicate", link, finishedlink
			else:
				noduplinksArray.append(link)
	return noduplinksArray
	
#print buildAlreadyFinishedArray()
	
	
	
#download_craigslist()
	
#if __name__ == "__main__":
#    if len(sys.argv) >= 2 and sys.argv[1] == "crawl":
#       if len(sys.argv) <= 2:
#            page_count = 1
#       else:
#            page_count = sys.argv[2]
#
#       if len(sys.argv) <= 3:
#            limit = 5
#       else:
#            limit = sys.argv[3]
#
#       print "Page Count: " + str(page_count)
#       print "Limit: " + str(limit)
#       #download_craigslist(int(page_count), int(limit))
#        #print json.dumps(download_craigslist(int(page_count), int(limit)))
#       # json.dump(json.dumps(download_craigslist(int(page_count), int(limit))), outfile)		   
#       for r in range(len(restaurants)):
#	   	   restaurant = restaurants[r]
#		   print restaurant
#	   	   userfile = open("cambridge_users.csv","a+")
#	   	   userwriter = csv.writer(userfile)
#	   	   timefile = open("cambridge_time.csv","a+")
#	   	   timewriter = csv.writer(timefile)
#	   	   locationfile = open("cambridge_location.csv","a+")
#	   	   locationwriter = csv.writer(locationfile)
#		   while True:
#			   try:
#				   download_craigslist(int(page_count), int(limit))
#			   except Exception, e:
#				   time.sleep(10)
#				   r+=1
#				   print e
#				   break
#		   
#    elif len(sys.argv) >= 2 and sys.argv[1] == "serve":
#        print "Server not implemented yet."
#    else:
#        print """
#Usage crawler: 
#    python craigslist.py crawl <page_count> <limit>
#
#Usage server:
#    python craigslist.py serve
#        """
#        