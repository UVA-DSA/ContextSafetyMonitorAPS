from subprocess import call
import json

algo_input_list = {"index":0,"BGTarget":125,"sens":45,"deltat_v":20,"dia":4,"dt":5.0,"time":1000,"bioavail":6.0,"Vg":253.0,"IRss":1.3,"events":{"bolus":[{ "    amt": 0.0, "start":250}],"basal":[{ "amt":0, "start":50,"length":30}],"carb":[{"amt":0.0,"start":0,"length":0},{"amt":0.0,"start":0,"length"    :0}]}}


with open("algo_input.json", "w") as write_algo_input_init:
	json.dump(algo_input_list, write_algo_input_init, indent=4)
	write_algo_input_init.close()


#call(["node","algo_bw.js"])
for _ in range(50):
	#with open("algo_input.json") as read_algo_input:	
	#with open("algo_input.json", "w") as algo_input:	
	if _ == 20:
		algo_input_list["events"]['basal'][0]['amt'] = 5
		algo_input_list["events"]['basal'][0]['start'] = 100

		
	with open("algo_input.json", "w") as write_algo_input:
		json.dump(algo_input_list, write_algo_input, indent=4)

#	print(algo_input_list['my_index'])	
	call(["node", "algo_bw.js"]);
	algo_input_list['index']=algo_input_list['index']+1
#	call(["node", "test_index.js"]);
