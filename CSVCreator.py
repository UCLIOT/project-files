import cloudant
import pprint
import json

account = cloudant.Account('ec5f2a2a-d88e-4358-8690-8349621cb9bd-bluemix')#The account is the first part of the hyperlink when you access the cloudant DB dashboard
database = account.database('traffic2')#This is the name of the database you create in cloudant for your data
f = open('sensordata2.csv','a')#Local file name for csv file
f.write("location,NO2Level,TSGAS,JamFactor,TSJAM,lat,lon,ts \n")
for doc in database.all_docs():
	j = json.loads(database.get(doc['id']).content)
	try:
		f.write(j['location']+","+j['NO2Level']+","+j['TSGAS']+","+j['JamFactor']+","+j['TSJAM']+","+j['lat']+","+j['lon']+","+j['ts']+" \n")# This will change depending on message data coming from the sensor
	except KeyError:
		print "KeyError"
f.close()
