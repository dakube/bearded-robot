#! /usr/bin/python3

#Phil.py
# v1.1
#Get info from wemineltc.com API and neatly print stuff on the console

import json
import urllib.request

def get_info(api):
	url="https://www.wemineltc.com/api?api_key="
	url_api = url + api #insane maths
	
	request = urllib.request.urlopen(url_api) # get some info
	dic = request.read()
	
	if dic == b'API Throttle In Effect!  Only 1 API Request Per 60 seconds is allowed.  Try again after 60 seconds.': 
		return False #Check if we are spamming and return False if we are
	
	data = json.loads(dic.decode('utf-8')) # parse from string to dict using json

	for key in data.keys(): 	#first pass in the dict
		if key == "workers": 	#get the "workers" key
			data2 = data[key]	#put the "workers" dict in the var data2
			#print (data2)		#data2 now possess workers info
	return data2

info = get_info("insert api key here")

#info = True

if info == False:
	print("Please wait 60 seconds") #Are we spamming? If you see this you are!
else:
	fmt = '{0:22} {1:10} {2:10}' #Format those strings
	print(fmt.format('worker', 'hashrate', 'alive')) #Top
	print() #space
	for i in info: #loop the info
		if info[i]['alive'] == "1": alive = "Yes" #replace 1 and 0 by Yes or No
		else: alive = "No"
		print(fmt.format(i, info[i]['hashrate'], alive )) #print in a neat little table
	
