import sys
import os
import LatencySheetEntry

resultDictionary = {}
latencySheetCache =[]

feature_list = [
'NO_OF_SUBMISSIONS',
'NO_OF_SUBMISSIONS_PROCESSED',
'NO_OF_SUBMISSIONS_PASSED',
'NO_OF_SUBMISSIONS_FAILED']

latencySheetAttribute = [
'APP_ID','APP_NAME','BADGE_KEY','BADGE_VALUE','START_DATE','LATENCY','END_DATE'
]

currentWeek ='22'
currentYear = '2016'

# git hub link https://github.com/MeenaCoder/WBRPython
"""
	NO_OF_SUBMISSIONS: No. of trophy apps submitted for the week under evaluation. 
"""
def evaluateNoOfSubmissions(fileName):

	lineCounter = []
	with open(fileName,'r') as submission_file:
		for line in submission_file:
			 lineCounter.extend(line.split('\r'))
			 
	print lineCounter
	# removing the header line
	print len(lineCounter)-1 
	resultDictionary['NO_OF_SUBMISSIONS']=len(lineCounter)-1 	
		
"""
	NO_OF_SUBMISSIONS_PROCESSED: No. of trophy apps pended or pushed live in the week under evaluation
"""
def evaluateNoSubmissionProcessed(fileName):
	
	lineCounter = []
	with open(fileName,'r') as submission_file:
		for line in submission_file:
			lineCounter.extend(line.split('\r'))
			 
	count =0
	# print lineCounter
	print len(lineCounter)	
	for entry in lineCounter:
		pass
		# print entry
		
		# singleSPEntry = entry.split(',')
		# print singleSPEntry
		# print '=====\n'
		# if singleSPEntry[62]!='Not Set' and singleSPEntry[0]!=currentWeek and currentYear not in singleSPEntry[1]:
			# pass
		# else:
			# count = count+1
			
	print count
			
		

def loadLatencySheet(fileName):
	lineCounter = []
	with open(fileName,'r') as submission_file:
		for line in submission_file:
			lineCounter.extend(line.split('\r'))
			# latency = LatencySheetEntry(latencyVal[0], latencyVal[1], latencyVal[2], latencyVal[3], latencyVal[4], latencyVal[5])
			# print latency
		for j in lineCounter:
			i = j.split(',')
			if i[0]!='APP_ID':
				print i
				cacheEntry = LatencySheetEntry.LatencySheetEntry(i[0],i[1],i[2],i[3],i[4],i[5],i[6])
				latencySheetCache.append(cacheEntry)
			
			
	print latencySheetCache
		
	
loadLatencySheet('C:\Users\meemeena@amazon.com\Desktop\WBR_TOOL\DataSource\Week22\LatencySheet.csv')

for i in latencySheetCache:
	print i.latency
	print i.appName
# evaluateNoSubmissionProcessed('C:\Users\meemeena@amazon.com\Desktop\WBR_TOOL\DataSource\Week22\TestingSharepoint.csv')
# print resultDictionary
	
	
	
	
# Utility method
