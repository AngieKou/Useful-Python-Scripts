#! /bin/env python

import sys
import os
import argparse

def createArgParser():
    Parser = argparse.ArgumentParser(description = 'Input Options for obtaining the poker profitability statistics')

    Parser.add_argument("-i", "--in",
                  dest="inputPath",
          default=False,
                  help="folder on which to run the script")

    Parser.add_argument("-u", "--username",
                  dest="userName",
          default=False,
                  help="username")
    return Parser

def parseArgs(args, argParser,):
	## parses the arguments
	argsList = argParser.parse_args(args)
	## gets the  related information
	argsDict = OrderedDict()
	argsDict['inputPath'] = argsList.inputPath
	argsDict['userName'] = argsList.userName
	return argsDict

def createArgParserAndParseArgs(localArgv,):
    Parser = createArgParser()
    argsDict = parseArgs(localArgv, Parser,)
    return argsDict

def main(localArgv):
	
	argsDict = createArgParserAndParseArgs(localArgv,)
	resultDir = argsDict['inputPath']
	userN = argsDict['userName']
	infoList = []
	infoTup = ()
	
	## reads in the tournament results 
	for (dirpath, dirname, files) in os.walk(resultDir):
	   for filename in files:
	   	inPut = resultDir+"/"+filename
	   	inFile = open(inPut, "r")
		for line in inFile:
			if line.startswith("Bu"):
				mon1 = line.split(":")[1].split("/")[0].strip("$ \n")
				mon2 = line.split(":")[1].split("/")[1].strip("$\n").replace(" USD", "")
		        	infoTup = (float(mon1)+float(mon2),)
			elif line.startswith("Free"):
				infoTup = infoTup + (int("0"),)
			elif "players" in line:
				infoTup = infoTup + (line.split(" ")[0],)
			elif userN in line:
				infoTup = infoTup + (line.split(":")[0],)
				if "$" in line:
					infoTup = infoTup + (line.split(",")[1].split("(")[0].strip("$ \n"),)
				else:
					infoTup = infoTup + ("0",)
		infoList.append(infoTup)

	##creates the outfile
        print infoList
	outFile = open("result.csv", "w")
	i=0
	outFile.write("Buy In ,Number of Players ,Final Position ,Money Made ")
	for tup in infoList:
		for item in infoTup:
			outfile.write(tup[0] + "," + tup[1] + "," + ",",tup[3]
			i +=1

	outFile.close
	return
   
if __name__ == '__main__':
    returnCode = main(sys.argv[1:])
    sys.exit(returnCode);
