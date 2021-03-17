import os
import os.path
import numpy as np
import time
from sys import argv

def insert_fault_code(fileLoc, faultLoc, codeline):
  brk = 0
  bkupFile = fileLoc+'.bkup'
  if os.path.isfile(bkupFile) != True:
    cmd = 'cp ' + fileLoc + ' ' + bkupFile
    os.system(cmd)
  else:
    print('Bkup file already exists!!')

  src_fp = open(fileLoc, 'w')
  bkup_fp = open(bkupFile, 'r')

  for line in bkup_fp:
    src_fp.write(line)
    if brk>0:
      for i in range(1, leadSp+1):
        src_fp.write(' ')
      src_fp.write('else:'+'\n')
      for l in np.arange(brk,len(codeline)):
        for i in range(1, leadSp+3):
          src_fp.write(' ')
        src_fp.write(codeline[l]+'\n')

    brk = 0

    if faultLoc in line:
      print ("injected 888")
      leadSp = len(line) - len(line.lstrip(' ')) # calculate the leading spaces

      for i in range(1, leadSp+1):
        src_fp.write(' ')
      src_fp.write(codeline[0]+'\n')

      for l in np.arange(1,len(codeline)):
        if codeline[l] != 'none\n':
          for i in range(1, leadSp+3):
            src_fp.write(' ')
          src_fp.write(codeline[l]+'\n')
        else:
          brk=l+1
          for i in range(1,3):
            src_fp.write(' ')
          break

  src_fp.close()
  bkup_fp.close()

def inject_fault(fileName):
  # global start_time_0
  in_file = fileName+'.txt'
  # outfile_path = 'out/'
  sceneLine  = fileName.split('_')
  sceneNum = sceneLine[len(sceneLine)-1]

  # # recFaultTime="//fltTime=open(\'out/fault_times.txt\',\'a+\')//fltTime.write(str(time.time())+\'||\')//fltTime.close()"
  # recFaultTime="//fltTime=open(\'out/fault_times.txt\',\'a+\')//fltTime.write(str(_)+\'||\')//fltTime.close()"

  # name_end = 0
  # name_id = []
  # fileNames = os.listdir("./result")
  # #rint("Num of Line",len(fileNames))
  # if len(fileNames) == 0:
  #   name_end = 0
  # else:
  #   for name in fileNames:
  #     name_id.append(int(((name.split('_')[1])).split('.')[0]))
  #   name_end = max(name_id)

  with open(in_file, 'r') as fp:
    print( in_file)
    line = fp.readline() # title line
    tLine = line.split('-')
    hz = tLine[len(tLine)-1].replace('\n','')
    title_num = line.split(':')
    scene_num = title_num[1].split('_')
    title = line.split(':')
    title[1] = title[1].replace('\n','')

    # if os.path.isdir('../output_files/'+title[1]) != True:
    #   os.makedirs('../output_files/'+title[1])

    # hazardFile = open('../output_files/'+title[1]+'/Hazards.txt','w')
    # alertFile = open('../output_files/'+title[1]+'/Alerts.txt','w')
    # summFile = open('../output_files/'+title[1]+'/summary.csv','w')

    # summLine = 'Scenario#,Fault#,Fault-line,Alerts,Hazards,T1,T2,T3\n'
    # summFile.write(summLine)

    # hazardFile.close()
    # alertFile.close()
    # summFile.close()

    # hazardFile = open('../output_files/'+title[1]+'/Hazards.txt','a+')
    # alertFile = open('../output_files/'+title[1]+'/Alerts.txt','a+')
    # summFile = open('../output_files/'+title[1]+'/summary.csv','a')

    line = fp.readline() # fault location line
    lineSeg = line.split('//')
    fileLoc = lineSeg[1]
    faultLoc = lineSeg[2]
    for line in fp:
      # line = line + recFaultTime
      lineSeg = line.split('//')
      startWord = lineSeg[0].split(' ')
      del lineSeg[0]

      if startWord[0]=='fault':
        print("+++++++++++"+title[1]+"++++++++++++++")
        # output_dir = '../output_files/'+title[1]+'/'+startWord[1]
        if 1:
        # if os.path.isdir(output_dir) != True:
        #   os.makedirs(output_dir)
          insert_fault_code(fileLoc, faultLoc, lineSeg)
          # print(os.getcwd())
          # os.system('ls')
#          cmd = 'python '+ 'updated_ct_script_iob_based_backup.py 200'
          os.system('./run_standalone_monitor.sh '+title[1]+' '+startWord[1]) #pass scenario and fault num to the .sh script

          '''Copy all output files in a common directory'''
          # cmd = 'cp -a ' + outfile_path+'/.' + ' ' + output_dir
          # os.system(cmd)

          if os.path.isdir('./simulation_data') == True:
            simulation_data_dir = './simulationCollection/'+title[1]+'/'+startWord[1]
            if os.path.isdir(simulation_data_dir) != True:
              os.makedirs(simulation_data_dir)
            cmd = 'mv -f ./simulation_data/* ' + ' ' + simulation_data_dir
            os.system(cmd)
            cmd = 'rm -rf ./simulation_data'
            os.system(cmd)
            
          
        # faultTime = 'N/A'
        # with open(output_dir+'/fault_times.txt') as fltFile:
        #   fltLine = fltFile.readline()  # first line
        #   fltTime = fltLine.split('||')
        #   if fltTime[0]=="":
        #     tm = -9999.
        #   else:
        #     tm = float(fltTime[0])


        # '''Write all alerts in single file '''
        # alertMsg = 'N/A'
        # alertTime = 'N/A'
        # startTime = 0
        # with open(output_dir+'/alerts.txt') as alFile:
        #   alLine = alFile.readline()  # first line
        #   alertFile.write('\nAlerts for fault '+startWord[1]+'::\n')
        #   for alLine in alFile:
        #     alertFile.write(alLine)
        #     if alLine.find('Glucose') >= 0:
        #       if tm >=0:
        #         # strTime = alLine.split('=')
        #       #   startTime = 0#start_time_0 #float(strTime[len(strTime)-1])
        #       # if startTime > 0.0:
        #         strTime = alLine.split('=')
        #         strAlert = alLine.split('||')
        #         if 1:
        #           if alertMsg == 'N/A':
        #             alertMsg = strAlert[1]
        #             alertTime = str(float(strTime[len(strTime)-1])-startTime)
        #           else:
        #             alertMsg = alertMsg +'||'+ strAlert[1]
        #             alertTime = alertTime+'||'+ str(float(strTime[len(strTime)-1])-startTime)
        # # if startTime==0.0:
        # #   alertMsg = 'Comma unavailable'
        # #   alertTime = str(startTime)


        # '''Write all hazards in single file '''
        # hazardMsg = 'N/A'
        # hazardTime = 'N/A'
        # with open(output_dir+'/hazards.txt') as hzFile:
        #   hazLine = hzFile.readline()  # first line
        #   hazardFile.write('\nHazards for fault '+startWord[1]+'::\n')
        #   for hazLine in hzFile:
        #     hazardFile.write(hazLine)
        #     hzTime = hazLine.split('=')
        #     hzTime = hzTime[len(hzTime)-1]
        #     hzTime = hzTime.replace('\n','')
        #     hzMsg = hazLine.split('||')
        #     if hazardMsg=='N/A':
        #       hazardMsg = hzMsg[1]
        #       hazardTime = str(float(hzTime) - startTime)
        #     else:
        #       hazardMsg = hazardMsg +'||'+ hzMsg[1]
        #       hazardTime = hazardTime +'||'+  str(float(hzTime) - startTime)


        # # calculate fault time
        # if tm <= -9999.:
        #   faultTime = 'N/A'
        # elif tm - startTime < 0:
        #   faultTime = '0'
        # else:
        #   faultTime = str(tm - startTime)


        # # delete the recFaultTime codes, don't want to store it in summary.csv
        # del lineSeg[len(lineSeg)-1]
        # del lineSeg[len(lineSeg)-1]
        # del lineSeg[len(lineSeg)-1]

        # faultLine = '||'.join(lineSeg)
        # faultLine = faultLine.replace('\n','')
        # summLine = '%d,%d,"%s",%s,%s,%s,%s,%s\n' %(int(sceneNum),int(startWord[1]),faultLine,alertMsg,hazardMsg,faultTime,alertTime,hazardTime)
        # summFile.write(summLine)

        #break
      # if "fault" in line:  
        # name_end = name_end+1
        # name_end_str = str(name_end)

        cmd = '> '+'data.csv'
        os.system(cmd)
        # cmd = 'python '+'updated_collected.py'
        # os.system(cmd)
        # cmd = 'cp '+'data.csv'+' ./result/data_%s.csv'%name_end_str
        # os.system(cmd)  

    # hazardFile.close()
    # alertFile.close()
    # summFile.close()
    
    print('Fault injection and execution done !!!')
    bkupFile = fileLoc+'.bkup'
    refFile = fileLoc+'.reference'       
    cmd = 'cp ' + fileLoc + ' ' + refFile
    os.system(cmd)
    cmd = 'cp ' + bkupFile + ' ' + fileLoc
    os.system(cmd)
    cmd = 'rm ' + bkupFile
    os.system(cmd)

  
start_time_0 = time.time()

if len(argv)>1:
  inject_fault(argv[1])
else:
  print('Fault library filename is missing, pass the filename as argument')

print('\n\n Total runtime: %f seconds' %(time.time()-start_time_0))

