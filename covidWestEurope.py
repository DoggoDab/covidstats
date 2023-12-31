import matplotlib.pyplot as plt 
import pandas as pd 
import seaborn as sns 
from matplotlib.ticker import FuncFormatter

sns.set()

dataCountries = ["United Kingdom", "France", "Germany", "Belgium", "Netherlands", "Luxembourg", "Switzerland", "Liechtenstein", "Austria", "Denmark", "Ireland", "Andorra", "Monaco"]
dataCases = [24812582, 40138560, 38758005, 4846040, 8623210, 388257, 4439992, 21561, 6081287, 3183756, 1726402, 48105, 17181]

data = {
    "countries": dataCountries, 
    "cases": dataCases
}

df = pd.DataFrame(data)

def formatfunc(value, _): 
    return f"{int(value):,}"

plt.figure(figsize=(20, 6))
counts = sns.barplot(x=df["countries"], y=df["cases"], data=df, label="Cases")

counts.yaxis.set_major_formatter(FuncFormatter(formatfunc))

for container in counts.containers: 
    counts.bar_label(container, fmt="%d", label_type="edge")

plt.show()