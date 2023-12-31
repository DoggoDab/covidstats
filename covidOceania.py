import matplotlib.pyplot as plt 
import pandas as pd 
import seaborn as sns 
from matplotlib.ticker import FuncFormatter 

sns.set()

dataCountries = ["Australia", "Papua New Guinea", "Fiji", "Solomon Islands", "Tuvalu", "Nauru", "Palau", "New Zealand", "Micronesia", "Samoa", "Vanuatu", "Tonga", "Marshall Islands", "Kiribati"]
dataCases = [11743801, 46864, 69117, 25954, 2943, 5393, 6265, 2541198, 26547, 16942, 12019, 16888, 16138, 5085]

data = {
    "countries": dataCountries, 
    "cases": dataCases
}

df = pd.DataFrame(data)

def formatfunc(value, _): 
    return f"{int(value):,}"

plt.figure(figsize=(20, 6))
counts = sns.barplot(x=df['countries'], y=df['cases'], data=df, label="Cases")

counts.yaxis.set_major_formatter(FuncFormatter(formatfunc))

for container in counts.containers: 
    counts.bar_label(container, fmt="%d", label_type="edge")

plt.show()