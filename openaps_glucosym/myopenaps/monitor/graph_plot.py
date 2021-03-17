import matplotlib
import pandas as pd
import json

with open("glucose.json", "r") as read_glucose:
	data = json.load(read_glucose)

#decemberMeans = [
#    {'year': 1948, 'temp': 271.24}, {'year': 1949, 'temp': 271.28},
#    {'year': 1950, 'temp': 268.52}, {'year': 1951, 'temp': 269.63},
#    {'year': 2015, 'temp': 277.23}, {'year': 2016, 'temp': 271.25}
#]  

df = pd.DataFrame(data)

plt.figure(1)
plt.plot(df['glucose'], df['date'], 'k-')
