import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.ticker import FuncFormatter

sns.set()

dataCountries = ["Turkmenistan", "Uzbekistan", "Tajikistan", "Kyrgyzstan", "Kazakhstan"]
dataCases = [0, 253662, 17786, 206897, 1411831]

data = {
    "countries": dataCountries, 
    "cases": dataCases, 
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