import matplotlib.pyplot as plt 
import pandas as pd 
import seaborn as sns 
from matplotlib.ticker import FuncFormatter 

sns.set()

dataCountries = ["Cameroon", "DRC", "Congo", "Equitorial \nGuinea", "Chad", "Burundi", "CAR", "Sao Tome \nand Principe", "Gabon"]
dataCases = [125242, 99333, 25375, 17229, 7701, 54721, 15440, 6743, 49501]

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