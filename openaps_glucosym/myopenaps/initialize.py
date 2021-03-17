import sys
from subprocess import call
import json
import datetime
import time

#initial_glucose = 300
initial_glucose = float(sys.argv[1])
rate = 0
duration = 30
min_ago_temp_delivered = 10

temp_has_initial_value = 1

glucose = [] 

#current_timestamp = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%dT%H:%M:%S-07:00') ## Original
current_timestamp = datetime.datetime.fromtimestamp(time.time()+4*60*60).strftime('%Y-%m-%dT%H:%M:%S-07:00') ## After time change

#current_timestamp = datetime.datetime.fromtimestamp(time.time()-(min_ago_temp_delivered*60)) # this is the time of 10 minutes (600 sec) ago
loaded_pump_history_to_dump = []	

if temp_has_initial_value:

	with open("monitor/pumphistory.json") as read_pump_history:
		loaded_pump_history = json.load(read_pump_history) # read whole pump_history.json
		pump_history_0 = loaded_pump_history[0].copy()	#load first element
		pump_history_1 = loaded_pump_history[1].copy() #load second element, fist and second are both for one temp basal
		pump_history_0['duration (min)'] = duration
		pump_history_1['rate'] = rate
		pump_history_0['timestamp'] = current_timestamp
		pump_history_1['timestamp'] = current_timestamp
		
		loaded_pump_history_to_dump.insert(0,pump_history_1)
		loaded_pump_history_to_dump.insert(0,pump_history_0)
	
	with open("monitor/pumphistory.json", "w") as write_pump_history:
		json.dump(loaded_pump_history_to_dump, write_pump_history, indent=4)

	
	with open("monitor/temp_basal.json") as read_temp_basal:
		loaded_temp_basal = json.load(read_temp_basal)
		loaded_temp_basal['rate'] = rate
		loaded_temp_basal['duration'] = (duration - min_ago_temp_delivered)
	
	with open("monitor/temp_basal.json", "w") as write_temp_basal:
		json.dump(loaded_temp_basal, write_temp_basal, indent=4)

else:

	with open("monitor/temp_basal.json") as read_temp_basal:
		loaded_temp_basal = json.load(read_temp_basal)
		loaded_temp_basal['rate'] = 0
		loaded_temp_basal['duration'] = 0
	
	with open("monitor/temp_basal.json", "w") as write_temp_basal:
		json.dump(loaded_temp_basal, write_temp_basal, indent=4)

	
	with open("monitor/pumphistory.json") as read_pump_history:
		loaded_pump_history = json.load(read_pump_history) # read whole pump_history.json
		pump_history_0 = loaded_pump_history[0].copy()	#load first element
		pump_history_1 = loaded_pump_history[1].copy() #load second element, fist and second are both for one temp basal
		pump_history_0['duration (min)'] = 0
		pump_history_1['rate'] = 0
		pump_history_0['timestamp'] = current_timestamp
		pump_history_1['timestamp'] = current_timestamp

		loaded_pump_history_to_dump.insert(0,pump_history_1)
		loaded_pump_history_to_dump.insert(0,pump_history_0)
	
	with open("monitor/pumphistory.json", "w") as write_pump_history:
		json.dump(loaded_pump_history_to_dump, write_pump_history, indent=4)



with open("monitor/glucose.json") as read_glucose:
	loaded_glucose = json.load(read_glucose)
	#print("loaded_glucose: ",loaded_glucose)
	loaded_glucose_first_element = loaded_glucose[0].copy()
	loaded_glucose_first_element["glucose"] = initial_glucose
	#print("loaded_glucose_first_element: ", loaded_glucose_first_element)	
	glucose.insert(0,loaded_glucose_first_element)

#print(glucose)
with open("monitor/glucose.json", "w") as write_glucose:
	json.dump(glucose, write_glucose, indent=4) 

#call(["cp", "initial_file/glucose.json", "monitor/"])
#call(["cp", "initial_file/pumphistory.json", "monitor/"])

to_glucosym = open('../glucosym/closed_loop_algorithm_samples/glucose_output_algo_bw.txt', 'w')
to_glucosym.write(str(initial_glucose))

#call(["python", "simplex_latest.py"])


