#!/usr/bin/python3.4
import sys
###########################
#This Python script reads a configuration file, cleans everything outside tags configuration.
#it receives as command line arguments the input file and output file names.
###########################
def xmlHeader (file_path):
	with open (file_path, 'wt') as myXML:
  	    myXML.write ('<?xml version="1.0" encoding="UTF-8"?>')
            myXML.write ('<!DOCTYPE tv SYSTEM "xmltv.dtd">')
	    myXML.write ('<tv generator-info-name="EPG"')
            myXML.write ('<tv generator-info-name="EPG" generator-info-url="http://www.epg.pt/" dvb-encoding="C">')
#	
def xmlFooter (file_path):
    with open(file_path, "at") as myXML	
        myXML.write ('</tv>')
#	
def wChannel (file_path,sid,name):
    with open(file_path, "at") as myXML	
        myXML.writeline ('<channel id=',sid, '>')
        myXML.writeline ('<display-name>',name,'></display-name></channel>')
#	
def wProgramme (file_path,starTime,stopTime,sid,title,subTitle,description):
    with open(file_path, "at") as myXML	
        myXML.writeline ('<programme start=',startTime, ' stop=',stopTime, ' channel=', sid,'>')
        myXML.writeline ('<title lang="Eng> "',title, '</title>')
        myXML.writeline ('<sub-title lang="Eng">',title, '</sub-title>')
        myXML.writeline ('<desc lang="Eng">',description, '</desc>')
        myXML.writeline ('</programme>')
#	
def openDirtyConfFile(input_file_path, output_file_path):
    myTagHead = "<configuration>"
    myTagFooter = "</configuration>"
    myNoHeadYet = -1
    postTagHead = -1	
    postTagFooter = -1	
    with open(input_file_path, "rt") as myIn:
        with open(output_file_path, "at") as myOut:
            for line in myIn:
                strTemp = line 
                if myNoHeadYet== -1: #If did not found yet the starting tag
                    posTagHead = strTemp.find(myTagHead) 
                    if posTagHead > -1:
                        strTemp = strTemp[posTagHead:]
                        myNoHeadYet = 1
                        posTagFooter = strTemp.find(myTagFooter) 
                        if posTagFooter > -1:
                            strTemp = strTemp[:postTagFooter+16]                    
                            myOut.write (strTemp)
                            break  
                        else:
                            myOut.write (strTemp)
                else:   #If had already found the starting tag  
                    posTagFooter = strTemp.find(myTagFooter) 
                    if posTagFooter > -1:
                        strTemp = strTemp[:postTagFooter+17]                    
                        myOut.write (strTemp)
                        break  
                    else:
                        myOut.write (strTemp) 
##############################
if __name__== "__main__":

    if len(sys.argv) > 1: #If has more than two arguments
        pathInput = sys.argv[1] #Get input file name
        pathOutput = sys.argv[2] #Get output file name
#
        xmlHeader(pathOutput) # Create the output file name with the first header
        openDirtyConfFile(pathInput,pathOutput) #Open the input file, clean it from the top and bottom trash and save it as a clean configuration 
        xmlFooter(pathOutput) # Create the footer on the xmltv file
#
	


	
