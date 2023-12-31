import matplotlib.pyplot as plt 
import pandas as pd 
import seaborn as sns 
from matplotlib.ticker import FuncFormatter 

sns.set()

dataCountries = ["Guatemala", "Belize", "Honduras", "Nicaragua", "Costa Rica", "El Salvador", "Panama"]
dataCases = [1280858, 71373, 474590, 18491, 1238883, 201833, 1049089]

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
    counts.bar_label(container, fmt="%d", label_type="edge")

plt.show()