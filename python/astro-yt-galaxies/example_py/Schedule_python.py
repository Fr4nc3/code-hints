#!/usr/bin/env python
# -*- coding: utf-8 -*
from xml.dom import minidom
import simplejson as json
from datetime import datetime
import pymongo
import numpy as np
import glob
import pytz
import sys
#import smbclient

#############################################################################
# To run, pythonb needs libsmbclient pysmbc   and have run the following:
#
# brew install libsmbclient
# python2.7 -m easy_install pysmbc
#
#############################################################################


#############################################################################
# XML scheduler reader  python Beta version March 2013
# Read Showtime Schedule XML from SMB envieronment 
# @author: friesco
#
#############################################################################

#############################################################################
# @variables are passing from the command line
# i.e python scheduleReader.py local 
# 
#############################################################################

variables = sys.argv
if len(variables) > 1:
   server = variables[1]
else:
   print variables
   print "Server parameter is missing"
   exit()


'''List of files'''
date_format = "%Y%m%d"

now = datetime.now()
base_date = datetime.strptime('20100101', date_format)
path = "/tmp/lineshoogle/"
XML_FILE = path + "SHOCom_Web_Guide_SHST"+now.strftime(date_format)+"*.XML"
Files = glob.glob(XML_FILE ) #Unique file
print Files
if len(Files) > 1: 
   print "More than one file "
   #exit()
    
XML = Files[0]







#############################################################################
# SAMBA connexion on Python
#############################################################################

#path = "\\nydcspsdb01.cbs.net\lineshoogle"
#user ="IBMSLinearRead"
#password ="R3adibms"
#
#server_ip = "nydcspsdb01.cbs.net" #"10.28.2.36"
#smb_structs.SUPPORT_SMB2 = True
#conn = SMBConnection(user, password, 'NYDCSPSDB01', "reader")
#conn.connect(server_ip,139)
#
#results = conn.listPath('', '/')
#
#XML_FILE = path + "SHOCom_Web_Guide_SHST"+now.strftime(date_format)+"*.XML"
#Files = glob.glob(XML_FILE) #Unique file


print "file name: " + XML
mongo_server ={}
mongo_server['monkey']   =  pymongo.Connection('129.228.131.249') 
mongo_server['qa-maint'] =  pymongo.Connection('qa-maint.sho.com') 
mongo_server['qa1']      =  pymongo.Connection('qa1.sho.com') 
mongo_server['local']      =  pymongo.Connection('127.0.0.1') 
mongo = pymongo.Connection('127.0.0.1') 
if server in mongo_server:
  mongo = mongo_server[server]
else:
  print "Missing Server name"
  exit()



#############################################################################
# Mongo DB connection
#############################################################################
#mongo = pymongo.Connection('qa-maint.sho.com') #qa-maint
mongo_db = mongo['taterstore']
mongo_collection = mongo_db['schedule']


xmldoc = minidom.parse(XML)
itemlist = xmldoc.getElementsByTagName('ROW') 
#############################################################################
#@string value check if value is empty or null
#return  null or text
#############################################################################
def IsNotNull(value):
    return value is not None and len(value) > 0

#############################################################################
# @xml tag  read tag text or  attribute 
# return text from attrinbute or tag
#############################################################################
def getText(tag):
    nodes = tag.childNodes
    for node in nodes:
        if node.nodeType == node.TEXT_NODE:
            s = node.data
            return s.strip(' \t\n\r').encode('utf-8')
        
#############################################################################
# @xml tag read tag children 
# return dictionary/ array built in base of XML tags
#############################################################################       
def getNode(tag):
    nodes = tag.childNodes
    array = []
    for node in nodes:
        if node.nodeType == node.ELEMENT_NODE:
          dict = {}
          for (name, value) in node.attributes.items():
              name = name.lower().decode("utf-8-sig") #.encode('utf-8')
              name_array = name.split("_")
              name = name_array[0]+name_array[1].title() + name_array[2].title()
              value = value.strip(' \t\n\r').encode('utf-8')
              dict[name] = value

          array.append(dict)
          
    return array    
              

#############################################################################
# @string datestring convert EST string to UTC time
# return dictionary built in base of XML tags
#############################################################################   
def convertDatetoUTC(datestring):
    utc     = pytz.utc
    eastern = pytz.timezone('US/Eastern')
    fmt     = "%Y-%m-%d %H:%M:%S %Z%z"
    date    = datetime.strptime(datestring,'%b %d %Y %H:%M:%S')
    date_eastern = eastern.localize(date,is_dst=None)
    date_utc     = date_eastern.astimezone(utc)
    #print datestring
    #print(date_utc.strftime(fmt))
    dates = {}
    #return an array with different formats
    dates['day']       = date_utc.strftime("%Y%m%d")

    ms = int(date.strftime("%s")) * 1000 

    dates['startTimeMilli'] = ms
    dates['startTime'] = date_utc.strftime("%H:%M:%S %Z%z")
    
    return dates

#############################################################################
# @string value check if content is series or movie
# note: there are more than this two type
# return string
#############################################################################  
def getType(value):
    if IsNotNull(value):
       return 'series'
    else:
        return 'movie'
    
    
    
#############################################################################
# @string value check if content is series or movie
# note: there are more than this two type
# return string
#############################################################################  
def isErotic(value):
    if value=="Erotic":
       return True
    else:
        return False
    
#############################################################################
# @string titleId
# note: images need to come from Oracle DB 
# return string url
#############################################################################      
def generateImageUrl(titleId,imagetype):
    #this should be different per each device 
    url= "http://www.sho.com/site/image-bin/images/0_0_"+ titleId +"/0_0_"+ titleId 
    if(imagetype=="popup"):
        url = url  +"_00_138x207.jpg"
    else:
         url = url  +"_00_100x100.jpg"
   # print url
    return url
#############################################################################
# @string titleId
# note: images need to come from Oracle DB 
# return string url
#############################################################################    
def generateImageUrlSeries(titleId,seasonNum,seriesId, imagetype):
    #this should be different per each device 
    #http://www.sho.com/site/image-bin/images/seriesID_seasonNum_titleID/seriesID_seasonNum_titleID_01_WxH.jpg

    url= "http://www.sho.com/site/image-bin/images/"+ seriesId +"_"+ seasonNum +"_"+ titleId +"/"+ seriesId +"_"+ seasonNum +"_" + titleId 
    
    if(imagetype=="popup"):
        url = url  + "_00_138x207.jpg"
    else:
         url = url  + "_00_100x100.jpg"
   # print url
    return url
#############################################################################
# @string hours convert hours in second in 24 hours format
# note: hour format #06:55:00
# return string seconds
#############################################################################  
def toSeconds(hours):
    #06:55:00
    pt     = datetime.strptime(hours, '%H:%M:%S')
    total_seconds = pt.second+pt.minute*60+pt.hour*3600
    return int(total_seconds)

#############################################################################
# @string description type, @xml tag
# return string description
############################################################################# 
def getDescription(descriptionType,tag):
    nodes = tag.childNodes
    for node in nodes:
        if node.nodeType == node.ELEMENT_NODE:
          dict = {}
          attr = node.getAttributeNode('TITLE_LTS_TARGET')
          attr_clean = attr.nodeValue.lower().encode('utf-8')
          descriptionType = descriptionType.lower()
          if descriptionType == attr_clean:
             attr_syn = node.getAttributeNode('TITLE_LTS_SYNOPSIS')
             desc =attr_syn.nodeValue.strip(' \t\n\r').encode('utf-8')
             #print desc
             return desc
         
    
#############################################################################
# Objects
# return string description
#############################################################################    
programs = []
days     = {}


#############################################################################
# READ THE XML and build the dictionaries 
# return @Dictionary
############################################################################# 
for s in itemlist :
    program                 =  {}
    date       = str(getText(s.getElementsByTagName("SCHEDULE_DATE")[0]).strip(' \t\n\r'))
    start_time =  str(getText(s.getElementsByTagName("START_TIME")[0]).strip(' \t\n\r'))
    #JUL 01 2012 06:55:00
    
    date_string  = date +" "+ start_time;
    
    UTCDate = convertDatetoUTC(date_string)
    print_date   = UTCDate['day'] #Ymd
    version_bref = getText(s.getElementsByTagName("VERSION_BREF")[0])
    titleId  = getText(s.getElementsByTagName("TITLE_BREF")[0])

    program["title"]        = getText(s.getElementsByTagName("PROGRAM")[0])
    program["start"]        = UTCDate['startTimeMilli'] 
    program["scheduleDate"] = print_date
    program["rating"]       = getText(s.getElementsByTagName("CERTIFICATE")[0])
    program["runTime"]      = toSeconds(getText(s.getElementsByTagName("VERSION_DURATION")[0]))
    program["titleID"]      = titleId
    program["releaseYear"]  = getText(s.getElementsByTagName("TITLE_PROD_YR")[0])


    #######################################################################################
    #BI elements 
    #######################################################################################
    program['bi'] = {}
    program['bi']["versionID"]   = version_bref
    program['bi']["isErotic"]    = isErotic(getText(s.getElementsByTagName("TITLE_GENRE")[0]))
     
    type                    = getType(getText(s.getElementsByTagName("SERIES_NAME")[0]))
    tag                     = s.getElementsByTagName("TITLE_LT_SETS")[0] 
    medium_description      = getDescription('Synopsis 256', tag)

    if IsNotNull(medium_description):
       program["descMedium"] =  medium_description 

    seasonNum         = getText(s.getElementsByTagName("SERIES_YR")[0]) 
    if (type == 'series'  and IsNotNull(seasonNum)):
       program["series"] = {}
       program["series"]["name"]   = getText(s.getElementsByTagName("SHOW_NAME")[0])
       episodeNum        =    getText(s.getElementsByTagName("EPISODE_NO")[0])
      
       seriesId       = getText(s.getElementsByTagName("SHOW_BREF")[0]) 
       seriesId = str(seriesId[4:])
       #(titleId,seasonNum,seriesId, imagetype):
       program["series"]["episodeNum"] = episodeNum 
       program["series"]["seasonNum"]  = seasonNum
       program["imageDisplay"]      = generateImageUrlSeries(titleId,seasonNum, seriesId,"display")
       program["imagePopUp"]        = generateImageUrlSeries(titleId,seasonNum, seriesId,"popup")
    else:
      program["imageDisplay"]       = generateImageUrl(titleId,"display")
      program["imagePopUp"]         = generateImageUrl(titleId,"popup")


    b = datetime.strptime(print_date, date_format)
    #print print_date
    delta1 = b - base_date
    delta = delta1.days
    #print "delta:" + str(delta)
    if  delta in days:
        days[delta].append(program)
    else:
         days[delta] = []
         days[delta].append(program)
    programs.append(program)    


#############################################################################
# Update Mongo with Days{Schedules}
# return void
############################################################################# 

for day in days:
    #print "day:" + str(day)
    print_date   = days[day][0]["scheduleDate"]
    #sort the programs 
    sortSchedule = sorted(days[day], key=lambda k: k['start']) 

    #check if the schedule day exist already in mongo:
    #if exist update schedule
    #if not insert  schedule
    date_exist = mongo_collection.find({'index' : long(str(day))})
    if date_exist.count() > 0:
        #update 
        print "updated :" + str(day)
        mongo_collection.update( {"index": long(str(day)) }, { "$set": { "json": json.dumps( sortSchedule, encoding="utf-8", ensure_ascii=False), "datetime":print_date}} )
    else:
        print "insert: " + str(day)
        insert
        insert_id = mongo_collection.insert({"index": long(str(day)),
                                             "datetime": print_date ,
                                             "active":1,
                                             "json": json.dumps(sortSchedule, encoding="utf-8", ensure_ascii=False)
                                             })


#
#print days
#print json.dumps(days, indent=4, encoding="utf-8", ensure_ascii=False)
