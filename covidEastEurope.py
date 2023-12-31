import matplotlib.pyplot as plt 
import pandas as pd 
import seaborn as sns 
from matplotlib.ticker import FuncFormatter 

sns.set()

dataCountries = ["Poland", "Bulgaria", "Russia", "Czechia", "Moldova", "Belarus", "Romania", "Hungary", "Ukraine", "Slovenia", "Albania", "Bosnia", "Serbia", "Croatia", "Montenegro", "Macedonia", "Kosovo", "Slovakia"]
dataCases = [6629601, 1333863, 23713738, 4744158, 628673, 994037, 3506590, 2223779, 5557995, 1354769, 334726, 403477, 2608125, 1279927, 295741, 350051, 273312, 1872391]

data = {
    "countries": dataCountries, 
    "cases": dataCases
}

df = pd.DataFrame(data)

def formatfunc(value, _): 
    return f"{int(value):,}"
    
fig, ax = plt.subplots(figsize=(10, 6))

plt.subplots_adjust(left=0.08, right=1)

counts = sns.barplot(x=df["countries"], y=df["cases"], data=df, label="Cases", ax=ax)

counts.yaxis.set_major_formatter(FuncFormatter(formatfunc))

for container in counts.containers: 
    counts.bar_label(container, fmt="%d", label_type="edge")

plt.show()