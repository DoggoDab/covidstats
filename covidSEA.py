import matplotlib.pyplot as plt
import pandas as pd 
import seaborn as sns
from matplotlib.ticker import FuncFormatter 

sns.set()

dataCountries = ["Vietnam", "Thailand", "Philippines", "Indonesia", "Singapore", "Malaysia", "Brunei", "Myanmar", "Laos", "Cambodia", "Timor-Leste"]
dataCases = [11624114, 4761781, 4134824, 6819830, 2827115, 5180812, 326275, 641422, 218906, 139003, 23460]

data = {
    "countries": dataCountries, 
    "cases": dataCases
}

df = pd.DataFrame(data)

def formatfunc(value, _): 
    return f"{int(value):,}"

plt.figure(figsize=(10, 6))
counts = sns.barplot(x=df["countries"], y=df["cases"], data=df, label='Cases')

counts.yaxis.set_major_formatter(FuncFormatter(formatfunc))

for container in counts.containers: 
    counts.bar_label(container, fmt="%d", label_type="edge")

plt.show()