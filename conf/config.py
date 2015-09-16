#!/usr/bin/env python
#----------------------------------------------------------------------------------
#
#
#
#
#----------------------------------------------------------------------------------
from libs import logs
import platform

OS = platform.system().upper()
niceOSPlataform = True if OS != "WINDOWS" else False
OSx = " [%s] :'( " % OS.upper() if niceOSPlataform == False else "[%s] <3" % OS.upper()

ftpRootFolder  = "C:\labGCBA" if niceOSPlataform == False else "/Users/jose/"
ftpRootFolder  = ftpRootFolder+"\\fftp" if niceOSPlataform == False else ftpRootFolder+"/fftp"
ftpGuessFolder = ftpRootFolder +"\\nobody" if niceOSPlataform == False else ftpRootFolder +"/nobody"
folderSeparator = "\\" if niceOSPlataform == False else ftpRootFolder +"/"
unitechFolder = "\\\\vmware-host\Shared Folders\Escritorio\EnviMan\Bin\Transfer\Data"

originDir = ""
ftpUser = "EPA"
ftpPass = "12345"
ftpHost = "127.0.0.1"
ftpPort = 21

validUser = False

EPAStationName = "Cordoba"
dataFileExt = '.otsf'
dataFileNameFormat = EPAStationName+'_T%Y%m%d%H%M'+dataFileExt
sensorFailure = -1

validUser = False
sensorId = 227

log = logs.log(EPAStationName,niceOSPlataform)
fileHeader = {}

version = {
    'anio': 2015,
    'menor': 0,
    'mayor': 1,
    'fase': 'BETA'
}

storeConf ="C:\labGCBA\pushEPAData\conf%s.epa" % EPAStationName

sensor_online = 1
sensor_offline = -1

sensors_st = {}
