import matplotlib.pyplot as plt 
import pandas as pd 
import seaborn as sns 
from matplotlib.ticker import FuncFormatter 

sns.set()

dataCountries = ['Burkina \nFaso', "Cote d'Ivoire", "Gambia", "Guinea \nBissau", "Guinea", "Mali", "Liberia", "Nigeria", "Sierre \nLeone", "Senegal", "Togo", "Benin", "Cabo \nVerde", "Ghana", "Niger"]
dataCases = [22107, 88380, 12626, 9614, 38572, 33162, 8090, 267173, 7766, 89033, 39531, 28036, 64477, 171889, 9931]

data = {
    "countries": dataCountries,
    "cases": dataCases
}

df = pd.DataFrame(data)

def formatfunc(value, _):
    return f"{int(value):,}"

plt.figure(figsize=(20, 6))
counts = sns.barplot(x=df['countries'], y=df['cases'], data=df, label='Cases')

counts.yaxis.set_major_formatter(FuncFormatter(formatfunc))

for container in counts.containers: 
    counts.bar_label(container, fmt='%d', label_type='edge')

plt.show()