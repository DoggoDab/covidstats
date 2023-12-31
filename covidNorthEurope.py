import matplotlib.pyplot as plt 
import pandas as pd 
import seaborn as sns 
from matplotlib.ticker import FuncFormatter 

sns.set()

dataCountries = ["Norway", "Estonia", "Lithuania", "Sweden", "Iceland", "Latvia", "Finland"]
dataCases = [1506672, 625771, 1385981, 2745098, 209503, 981106, 1511701]

data = {
    "countries": dataCountries, 
    "cases": dataCases
}

df = pd.DataFrame(data)

plt.figure(figsize=(10, 6))

def formatfunc(value, _): 
    return f"{int(value):,}"

counts = sns.barplot(x=df['countries'], y=df['cases'], data=df, label="Cases")

counts.yaxis.set_major_formatter(FuncFormatter(formatfunc))

for container in counts.containers: 
    counts.bar_label(container, fmt="%d", label_type="edge")

plt.show()