import matplotlib.pyplot as plt 
import pandas as pd 
import seaborn as sns 
from matplotlib.ticker import FuncFormatter 

sns.set()

dataCountries = ["Argentina",  "Uruguay", "Paraguay", "Brazil", "Venezuela", "Guyana", "Chile", "Ecuador", "Colombia", "Peru", "Suriname", "Bolivia"]
dataCases = [10080046, 1041111, 822337, 38177375, 552695, 73679, 5330856, 1070121, 6386157, 4524326, 82588, 1210892]

data = {
    "countries": dataCountries, 
    "cases": dataCases
}

df = pd.DataFrame(data)

def formatfunc(value, _): 
    return f"{int(value):,}"

plt.figure(figsize=(10, 6))
counts = sns.barplot(x=df['countries'], y=df['cases'], data=df, label="Cases")

counts.yaxis.set_major_formatter(FuncFormatter(formatfunc))

for container in counts.containers: 
    counts.bar_label(container, fmt='%d', label_type="edge")

plt.show()