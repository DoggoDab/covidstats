import matplotlib.pyplot as plt 
import pandas as pd 
import seaborn as sns 
from matplotlib.ticker import FuncFormatter 

sns.set()

dataCountries = ["Italy", "Portugal", "Greece", "Vatican City", "San Marino", "Spain", "Malta"]
dataCases = [26591441, 5635112, 6101379, 29, 25292, 13914811, 120935]

data = {
    "countries": dataCountries, 
    "cases": dataCases
}

df = pd.DataFrame(data)

def formatfunc(value, _): 
    return f"{int(value):,}"

plt.figure(figsize=(10, 6))
counts = sns.barplot(x=df["countries"], y=df["cases"], data=df, label="Cases")

counts.yaxis.set_major_formatter(FuncFormatter(formatfunc))

for container in counts.containers: 
    counts.bar_label(container, fmt="%d", label_type="edge")

plt.show()