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
duplicates = []
latestDictionary = {}

detroit = ["48226"]
locationDict = {}
laZips_geo = ["90002", "90003", "90004", "90005", "90006", "90007", "90008", "90010", "90011", "90012", "90013", "90014", "90015", "90016", "90017", "90018", "90019", "90020", "90021", "90022", "90023", "90024", "90025", "90026", "90027", "90028", "90029", "90031", "90032", "90033", "90034", "90035", "90036", "90037", "90038", "90039", "90040", "90041", "90042", "90043", "90044", "90045", "90046", "90047", "90048", "90049", "90056", "90057", "90058", "90059", "90061", "90062", "90063", "90064", "90065", "90066", "90067", "90068", "90069", "90071", "90073", "90077", "90089", "90094", "90095", "90201", "90210", "90211", "90212", "90220", "90221", "90222", "90230", "90232", "90240", "90241", "90242", "90245", "90247", "90248", "90249", "90250", "90254", "90255", "90260", "90261", "90262", "90263", "90265", "90266", "90270", "90272", "90274", "90275", "90277", "90278", "90280", "90290", "90291", "90292", "90293", "90301", "90302", "90303", "90304", "90305", "90401", "90402", "90403", "90404", "90405", "90501", "90502", "90503", "90504", "90505", "90506", "90601", "90602", "90603", "90604", "90605", "90606", "90623", "90630", "90631", "90638", "90639", "90640", "90650", "90660", "90670", "90701", "90703", "90704", "90706", "90710", "90712", "90713", "90715", "90716", "90717", "90723", "90731", "90732", "90744", "90745", "90746", "90747", "90755", "90802", "90803", "90804", "90805", "90806", "90807", "90808", "90810", "90813", "90814", "90815", "90822", "90831", "90840", "90846", "91001", "91006", "91007", "91008", "91010", "91011", "91016", "91020", "91023", "91024", "91030", "91040", "91042", "91046", "91101", "91103", "91104", "91105", "91106", "91107", "91108", "91125", "91126", "91201", "91202", "91203", "91204", "91205", "91206", "91207", "91208", "91210", "91214", "91301", "91302", "91303", "91304", "91306", "91307", "91311", "91316", "91321", "91324", "91325", "91326", "91330", "91331", "91335", "91340", "91342", "91343", "91344", "91345", "91350", "91351", "91352", "91354", "91355", "91356", "91361", "91362", "91364", "91367", "91381", "91382", "91384", "91387", "91390", "91401", "91402", "91403", "91405", "91406", "91411", "91423", "91436", "91501", "91502", "91504", "91505", "91506", "91521", "91522", "91523", "91601", "91602", "91604", "91605", "91606", "91607", "91608", "91702", "91706", "91709", "91710", "91711", "91722", "91723", "91724", "91731", "91732", "91733", "91740", "91741", "91744", "91745", "91746", "91748", "91750", "91754", "91755", "91759", "91765", "91766", "91767", "91768", "91770", "91773", "91775", "91776", "91780", "91789", "91790", "91791", "91792", "91801", "91803", "92397", "92821", "92823", "93243", "93510", "93523", "93532", "93534", "93535", "93536", "93543", "93544", "93550", "93551", "93552", "93553", "93563", "93591"]
nycZips_geo =["11372","11004","11040","11426","11365","11373","11001","11375","11427","11374","11366","11423","11428","11432","11379","11429","11435","11415","11418","11433","11451","11221","11421","11419","11434","11216","11416","11233","11436","11213","11212","11225","11218","11226","11219","11210","11230","11204","10471","10470","10466","10467","10463","10475","10464","10469","10468","10463","10458","10034","10033","10462","10040","10453","10465","10464","10464","10461","10457","10460","10032","10452","10456","10472","10031","10039","10459","10451","10473","10030","10027","10474","10455","10037","10024","10454","10026","10035","10025","10035","11357","10029","00083","11356","11359","11360","11105","10128","11371","10023","11363","10028","11354","11102","11370","10021","11361","11358","11362","10044","11369","11103","11106","11368","11377","10036","11355","11101","11364","10018","10020","11005","10017","10001","10011","10016","11104","11109","10010","11367","10014","10003","11222","10002","11378","10009","10012","10013","11211","10007","11237","11385","10038","11206","10006","11412","10005","11251","10004","11411","11201","10004","11205","11208","11207","10004","10004","11413","11217","11238","11231","11422","11420","11417","11215","11414","11231","11232","11430","11203","11239","11236","11220","10301","10310","10303","11234","10302","11693","11209","10304","10314","11693","11228","11096","10305","11229","11214","11691","11096","11223","11693","11692","11235","11693","10306","11694","11224","10308","11697","10312","10309","10307","10280","10048","10279","10165","10168","10055","10105","10118","10176","10162","10019","10111","10170","10112","10122","10107","10103","10153","10174","10166","10169","10167","10177","10172","10171","10154","10152","10270","10104","10271","10110","10175","10151","10173","10178","10119","10121","10115","10123","10106","10158","10041","10120","10278","10155","10022","10043","10081","10096","10097","10196","10196","10275","10265","10045","10047","10047","10080","10203","10259","10260","10285","10286","11370","10065","10075","10069","10281","10282"]
nycZips_post =["11201", "11202", "11203", "11204", "11205", "11206", "11207", "11208", "11209", "11210", "11211", "11212", "11213", "11214", "11215", "11216", "11217", "11218", "11219", "11220", "11221", "11222", "11223", "11224", "11225", "11226", "11228", "11229", "11230", "11231", "11232", "11233", "11234", "11235", "11236", "11237", "11238", "11239", "11240", "11241", "11242", "11243", "11244", "11245", "11247", "11248", "11249", "11251", "11252", "11254", "11255", "11256", "10001", "10002", "10003", "10004", "10005", "10006", "10007", "10008", "10009", "10010", "10011", "10012", "10013", "10014", "10015", "10016", "10017", "10018", "10019", "10020", "10021", "10022", "10023", "10024", "10025", "10026", "10027", "10028", "10029", "10030", "10031", "10032", "10033", "10034", "10035", "10036", "10037", "10038", "10039", "10040", "10041", "10043", "10044", "10045", "10046", "10047", "10048", "10055", "10060", "10065", "10069", "10072", "10075", "10079", "10080", "10081", "10082", "10087", "10090", "10094", "10095", "10096", "10098", "10099", "10101", "10102", "10103", "10104", "10105", "10106", "10107", "10108", "10109", "10110", "10111", "10112", "10113", "10114", "10115", "10116", "10117", "10118", "10119", "10120", "10121", "10122", "10123", "10124", "10125", "10126", "10128", "10129", "10130", "10131", "10132", "10133", "10138", "10149", "10150", "10151", "10152", "10153", "10154", "10155", "10156", "10157", "10158", "10159", "10160", "10161", "10162", "10163", "10164", "10165", "10166", "10167", "10168", "10169", "10170", "10171", "10172", "10173", "10174", "10175", "10176", "10177", "10178", "10179", "10184", "10185", "10196", "10197", "10199", "10203", "10211", "10212", "10213", "10242", "10249", "10256", "10257", "10258", "10259", "10260", "10261", "10265", "10268", "10269", "10270", "10271", "10272", "10273", "10274", "10275", "10276", "10277", "10278", "10279", "10280", "10281", "10282", "10285", "10286", "10292", "11692", "11102", "11103", "11105", "11106", "11359", "11360", "11361", "11426", "11697", "11411", "11356", "11368", "11369", "11370", "11373", "11380", "11690", "11691", "11693", "11695", "11002", "11005", "11351", "11352", "11354", "11355", "11358", "11367", "11371", "11381", "11390", "11375", "11365", "11366", "11004", "11423", "11414", "11372", "11405", "11424", "11425", "11430", "11431", "11432", "11433", "11434", "11435", "11436", "11439", "11451", "11499", "11415", "11362", "11363", "11101", "11109", "11120", "11378", "11379", "11364", "11416", "11417", "11427", "11428", "11429", "11374", "11418", "11385", "11386", "11694", "11422", "11412", "11420", "11419", "11413", "11104", "11357", "11421", "11377", "10301", "10302", "10303", "10304", "10305", "10306", "10307", "10308", "10309", "10310", "10311", "10312", "10313", "10314", "10451", "10452", "10453", "10454", "10455", "10456", "10457", "10458", "10459", "10460", "10461", "10462", "10463", "10464", "10465", "10466", "10467", "10468", "10469", "10470", "10471", "10472", "10473", "10474", "10475", "10499"]
#cambridge_zipcodes = ["02138" ]
cambridge_zipcodes =["02139", "02140", "02141", "02142"]
boston = ["02112","02113", "02114"]
#http://www.yelp.com/search?find_desc=&find_loc=02139&ns=1&ls=a43b5ee92455361c#cflt=restaurants

page = [35,4,92,71,87,76,38,84,91,7,13,86,40,19,43,37,44,8,62,66,10,28,31,90,32,93,33,20,53,63,79,34,22,74,80,11,98,52,78,54,56,59,68,1,72,17,50,36,2,95,29,96,6,61,81,24,97,48,14,65,3,51,88,23,57,69,46,77,26,41,85,27,55,73,75,45,82,49,15,16,25,12,47,60,5,42,18,94,70,39,99,64,89,58,67,21,30,9,83]
pageNumber = 0
i = 0

def download_craigslist(page_count = 1, limit = 5):
	art = []
	data = []
	page_count = len(page)
	#get list of restaurants  on page
	for i in range(page_count):
		pageNumber = page[i]
		print pageNumber,i
		base1 = "http://www.yelp.com/search?find_desc=&find_loc="
        #zipcode = zipcode
		base2 = "&start="
		pageIndex = str(pageNumber*10)
		base3 = "&cflt="
		category = "restaurants"
		url = base1+zipcode+base2+pageIndex+base3+category
		print url
		soup = BeautifulSoup(urllib2.urlopen(url).read())
		x = soup.find_all("a",{"class":"biz-name"})
		#print x
		if len(x)<1:
			return
		i = i+1
		for line in x:
			line = str(line).split("href=")[1]
			restaurantLink = line.split(">")[0]
			restaurantName = line.split(">")[1]
			if "adredir" not in str(line):
				print line
				spamwriter.writerow([restaurantLink])
		time.sleep(random.random()*10)
				
       # addresses = soup.find_all("div",{"class":"secondary-attributes"})
       # for address in addresses:
	   #		address = re.sub("<.*?>"," ",str(address))
	   #		address = re.sub(r"[\xc2\xa0\xe2\x80\x99]","",address)
	   #		address = " ".join(address.split())
	   #		print address

if __name__ == "__main__":
    if len(sys.argv) >= 2 and sys.argv[1] == "crawl":
       if len(sys.argv) <= 2:
            page_count = 1
       else:
            page_count = sys.argv[2]

       if len(sys.argv) <= 3:
            limit = 5
       else:
            limit = sys.argv[3]

       print "Page Count: " + str(page_count)
       print "Limit: " + str(limit)  
       for j in range(len(boston)):
	   	   zipcode = boston[j]
	   	   outputfile = open("boston_restaurantLinks"+zipcode+".csv","a+")
	   	   spamwriter = csv.writer(outputfile)
		   while True:
			   try:
				   download_craigslist(int(page_count), int(limit))
			   except Exception, e:
				   time.sleep(10)
				   j+=1
				   print e
				   break
       
    elif len(sys.argv) >= 2 and sys.argv[1] == "serve":
        print "Server not implemented yet."
    else:
        print """
Usage crawler: 
    python craigslist.py crawl <page_count> <limit>

Usage server:
    python craigslist.py serve
        """
        