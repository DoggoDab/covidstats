import matplotlib.pyplot as plt 
import pandas as pd 
import seaborn as sns 
from matplotlib.ticker import FuncFormatter 

sns.set()

dataCountries = ["Botswana", "Mozambique", "Eswatini", "Zimbabwe", "Zambia", "Angola", "Lesotho", "Malawi", "South \nAfrica", "Namibia"]
dataCases = [330413, 233731, 75189, 265975, 349304, 106303, 35892, 89168, 4076463, 172221]

data = {
    "countries": dataCountries, 
    "cases": dataCases
}

df = pd.DataFrame(data)

def formatfunc(value, _): 
    return f"{int(value):,}"

plt.figure(figsize=(15, 6))
counts = sns.barplot(x=df['countries'], y=df['cases'], data=df, label='Cases')

counts.yaxis.set_major_formatter(FuncFormatter(formatfunc))

for container in counts.containers: 
    counts.bar_label(container, fmt='%d', label_type='edge')

plt.show()