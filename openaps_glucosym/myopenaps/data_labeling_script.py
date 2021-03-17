
# coding: utf-8

# #  <p style="text-align: center;"><span style="background-color: #FFFF00"><u> Data Visualization and Analysis </u></span></p>

# In[23]:


import pandas as pd
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
#from matplotlib import pyplot as plt
#from sklearn.preprocessing import StandardScaler
import numpy as np
#import cv2
#from sklearn.preprocessing import MinMaxScaler
import math

BGT=120
MaxBG = 180
MinBG = 70
RiskUpLimit = 50
RiskLowLimit = 0

file_name = "data.csv"


# ## <p style="text-align: center;"><span style="background-color: #FFFF00"><u> Context Table </u></span></p>
# <img src="context_table.png" width="700"/>

# # <span style="background-color: #FFFF00"><u> Load the simulated data </u></span>

# In[24]:


data = pd.read_csv(file_name, error_bad_lines=False)
#filtered_loaded_data = loaded_data.filter(["bg", "CGM_glucose", "IOB", "rate", "running_temp"], axis=1)
#data = loaded_data.filter(["bg", "CGM_glucose", "IOB", "rate", "running_temp", "unsafe_action_reason"], axis=1)


# In[25]:


#data["eq_glucose"] = data["CGM_glucose"]-45*data["IOB"]
#data["BGT"] = BGT
#data["MaxBG"] = MaxBG
#data["MinBG"] = MinBG


# ## <span style="background-color: #FFFF00"><u> Risk Index calculation using following formula </u></span>
# <b>BGT</b> = 120 in this case. It is patient dependent and comes from physician.  <br />
# <b>MaxBG</b> = 180, Maximum glucose level above which it is treated as hyperglycemia.Comes from literature.  <br />
# <b>MinBG</b> = 70, Minimum glucose level under which it is treated as hypoglycemia. Comes from literature. <br />
# 
# <b>UnderDose_risk_index (OD_Index)</b> = (CGM_glucose - BGT)/(MaxBG - BGT)  <br />
# <b>OverDose_risk_index (UD_Index)</b> = (BGT - CGM_glucose)/(BGT - MinBG)

# In[26]:


# data["OD_index"] = 0
# data["UD_index"] = 0
# data["OD_index"] = data["OD_index"].astype(float)
# data["UD_index"] = data["UD_index"].astype(float)
# for i in range(len(data)-1):
    # #print(i)
    # #print(filtered_loaded_data["CGM_glucose"][i])
    # #print((float(filtered_loaded_data["CGM_glucose"][i+1])-float(BGT))/(float(MaxBG)-float(BGT)))
    # data["UD_index"][i] = (data["CGM_glucose"][i+1]-BGT)/(MaxBG-BGT)
    # data["OD_index"][i] = (BGT-data["CGM_glucose"][i+1])/(BGT-MinBG)
    
# data["UD_index"][len(data)-1] = data["UD_index"][len(data)-2]
# data["OD_index"][len(data)-1] = data["OD_index"][len(data)-2]


# # In[27]:


# data["rate"] = 100*data["rate"]
# data["OD_index"] = 50*data["OD_index"]
# data["UD_index"] = 50*data["UD_index"]
# data["IOB"] = 100*data["IOB"]


# ## <span style="background-color: #FFFF00"><u> Risk Index Calculation with the formula used in "Simglucose" simulator </u></span>
# <img src="risk_index_formula_simglucose.png" width = "450"/>

# In[28]:


rl_bg = []
rh_bg = []
LBGI = []
HBGI = []

for i in data["CGM_glucose"]:
    f_bg = 1.509*(math.pow((math.log(i)), 1.084) - 5.381)
    r_bg = 10*math.pow(f_bg, 2)
    
    if f_bg < 0:
        rl_bg.append(r_bg)
    else:
        rl_bg.append(0)
    
    if f_bg > 0:
        rh_bg.append(r_bg)
    else:
        rh_bg.append(0)
    
    LBGI.append(sum(rl_bg)/len(rl_bg))
    HBGI.append(sum(rh_bg)/len(rh_bg))

data["LBGI"] = LBGI
data["HBGI"] = HBGI
data["BGI"] = [i+j for i,j in zip(HBGI, LBGI)]


# ## Scale LBGI and HBGI to plot

# In[29]:


data["LBGI"] = 5*data["LBGI"]
data["HBGI"] = 5*data["HBGI"]
data["BGI"] = 10*data["BGI"]


# In[30]:


#data.head()


# ## <span style="background-color: #FFFF00"><u> Slope Calculation </u></span>

# In[31]:


#data["Slope"] = 0
#data["Slope"] = data["Slope"].astype(float)
#for i in range(len(data)-2):
#    data["Slope"][i] = (data["BGI"][i+1]-data["BGI"][i])/5
#data["Slope"][len(data)-2] = data["Slope"][len(data)-3]
#data["Slope"][len(data)-1] = data["Slope"][len(data)-2]
#data["Slope"] = 1000*data["Slope"]


# In[32]:


#data.head(20)


# ## <span style="background-color: #FFFF00"><u> Data Labeling </u></span>

# In[33]:


#data["Label"] = 0
#data["Label"] = data["OD_index"].astype(float)
#for i in range(len(data)-1):
#    if (data["BGI"][i+1])-data["BGI"][i] >=1:
#        data["Label"][i] = 100
#    else:
#        data["Label"][i] = 0
#data["Label"][len(data)-1] = data["Label"][len(data)-2]

data["Label"] = 0
data["Label"] = data["Label"].astype(float)
for i in range(len(data)-2):
    if (data["BGI"][i+2]-data["BGI"][i] >=0.45):
        data["Label"][i] = 100
    else:
        data["Label"][i] = 0
data["Label"][len(data)-2] = data["Label"][len(data)-3]
data["Label"][len(data)-1] = data["Label"][len(data)-2]


# In[34]:


#data.head()


# In[35]:


#label = [0]
#for i in range(len(data["BGI"])-1):
#    if ((data["BGI"][i+1]-data["BGI"][i])>=1):
#        label.append(100)
#    else:
#        label.append(0)
#data["Label"] = label


# In[36]:


#data.head()


# In[37]:

#data["Label"].sum()



# ## <span style="background-color: #FFFF00"><u> Save labeled data to csv file </u></span>

# In[38]:


#data.to_csv("labeled_"+file_name)


# In[39]:


# num_label = 0
# data_rows_of_positive_label = []
# for i in range(len(data.index)):
    # if data["Label"][i] != 0:
        # num_label +=1
        # data_rows_of_positive_label.append(i)
#data.loc[data_rows_of_positive_label]


# In[40]:


# risk_up_limit = [RiskUpLimit]*len(data.index)
# risk_low_limit = [RiskLowLimit]*len(data.index)


# ## <span style="background-color: #FFFF00"><u> Rows having Unsafe action reason </u></span>

# In[41]:


violation = 0
data_rows_of_violation = []
for i in range(len(data.index)):
    if data["unsafe_action_reason"][i] != "Null":
        violation +=1
        data_rows_of_violation.append(i)
#data.loc[data_rows_of_violation]


# In[42]:

data["detection"] = data["unsafe_action_reason"];
for index,row in data.iterrows():
	if data.at[index,"detection"] == "Null":
		data.at[index,"detection"] = 0
	else:
		data.at[index,"detection"] = 100
# #data.head()

data.to_csv("labeled_"+file_name)

# In[43]:


#data.head()


# In[44]:


# plt.figure(figsize=(15,10))
# plt.plot(data.index, data["bg"], linewidth=2, label="blood_glucose", color='m')
# plt.plot(data.index, data["eq_glucose"], linewidth=2, label="eq_glucose", color='m')
# #plt.plot(data.index, data["IOB"], linewidth=2, label="IOB")
# plt.plot(data.index, data["CGM_glucose"], linewidth=2, label="cgm_glucose", color = 'b')
# plt.plot(data.index, data["rate"], linewidth=2, label="insulin_rate*100", color='k')
# #plt.plot(data.index, data["OD_index"], linewidth=2, label="OverDoase_risk_index*50", color='r')
# #plt.plot(data.index, data["UD_index"], linewidth = 2, label="UnderDose_risk_index*50", color='y')
# plt.plot(data.index, data["BGT"], linewidth = 2, label="BGT", linestyle="--", color = 'g')
# plt.plot(data.index, data["MaxBG"], linewidth = 2, label="MaxBG", linestyle="--", color = 'b')
# plt.plot(data.index, data["MinBG"], linewidth = 2, label="MinBG", linestyle="--", color = 'b')
# #plt.plot(filtered_loaded_data.index, filtered_loaded_data["HBGI"], linewidth = 2, label="HBGI*5")
# #plt.plot(filtered_loaded_data.index, filtered_loaded_data["LBGI"], linewidth = 2, label="LBGI*5")
# plt.plot(data.index, data["BGI"], linewidth = 2, label="BGI*5", color = 'y')
# plt.plot(data.index, risk_up_limit, linewidth = 2, label="risk_up_limit", linestyle="--", color = 'r')
# plt.plot(data.index, risk_low_limit, linewidth = 2, label="risk_low_limit", linestyle="--", color = 'm')
# plt.stem(data.index, data["unsafe_action_reason"])
# plt.stem(data.index, data["Label"], 'g')
# #plt.plot(data.index, data["Slope"], 'b')
# plt.legend()
# plt.show()


# # In[45]:


# print("Simulation time: ", len(data)*5, " minutes")
# print("Number of unsafe control actions: ", violation)

