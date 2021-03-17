import numpy as np
from  sklearn.metrics import f1_score
import pandas as pd

partFileName = "data_patientA_"
ig = [80, 100, 120, 140, 160, 180, 200, 220, 240, 260, 280, 300, 320]

for i in ig:
	data = pd.read_csv(partFileName+str(i)+".csv",error_bad_lines = False)
	y_pred = np.array(data["detection"].tolist())
	y_true = np.array(data["Label"].tolist())
	
	writeFile_F1 = open("f1_score_"+str(i)+".txt", "w+")
	writeFile_F1.write(str(f1_score(y_true, y_pred, average=None)))
	

