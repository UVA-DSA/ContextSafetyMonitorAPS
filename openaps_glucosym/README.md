# This is code repository for openaps simulation

run the commands on a terminal

"cd myopenaps"
"git init"
"cd ../glucosym"
"npm start"


open a browser and go to website "http://localhost:3000/" and set the initial Glucose level
open a new terminal and run:
"cd myopenaps"
option1:
"sudo ./run_fault_campain_xx.sh"(comment some lines if you just want to test parts of the experiments in the shell script)
option 2:
"sudo -s
"./run_fault_campain_xx.sh"

note: 
1. make sure the init value in run_standalone.sh is the same with that you set in the browser
2. If you are runing this simulation on VMware Player. you may face some problems of frequent network disconnection and reconnection which will interrupt the experiments. So you can change the network mode from NAT to Bridge connect and also check the duplicate physical nework choice, and disable the network.
3. /openaps_monitor/glucosym/views/index.jade change patient j
4. change port number in /openaps_monitor/glucosym/bin/www if facing port confliction.