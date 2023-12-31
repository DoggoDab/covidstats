import matplotlib.pyplot as plt 
import pandas as pd 
import seaborn as sns 
from matplotlib.ticker import FuncFormatter 

sns.set()

dataCountries = ["Armenia", "Azerbajian", "Bahrain", "Cyprus", "Georgia", "Iraq", "Iran", "Israel", "Jordan", "Kuwait", "Lebanon", "Oman", "Palestine", "Qatar", "Saudi Arabia", "Syria", "Turkey", "UAE", "Yemen"]
dataCases = [451353, 834259, 729549, 660854, 1855289, 2465545, 7625292, 4841772, 1746997, 666586, 1243838, 399449, 621008, 514524, 841469, 57743, 17232066, 1067030, 11945]

data = {
    "countries": dataCountries,
    "cases": dataCases
}

df = pd.DataFrame(data)

def formatfunc(value, _): 
    return f"{int(value):,}"

plt.figure(figsize=(25, 6))
counts = sns.barplot(x=df["countries"], y=df["cases"], data=df, label="Cases")

counts.yaxis.set_major_formatter(FuncFormatter(formatfunc))

for container in counts.containers: 
    counts.bar_label(container, fmt="%d", label_type="edge")

plt.show()