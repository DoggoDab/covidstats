import matplotlib.pyplot as plt 
import pandas as pd 
import seaborn as sns
from matplotlib.ticker import FuncFormatter 

sns.set()

dataCountries = ["Canada", "Mexico", "Bahamas", "Jamaica", "United States", "Cuba", "Haiti", "Dominican", "Barbados", "Antigua \nBarbuda", "Dominica", "Grenada", "Kitts Nevis", "Lucia", "Vincent \nGrenedines", "Trinidad \nTobago"]
dataCases = [4855902, 7702731, 38084, 156573, 110102732, 1115175, 34501, 670627, 110277, 9106, 16038, 19693, 6607, 30209, 9674, 191496]

data = {
    "countries": dataCountries, 
    "cases": dataCases 
}

df = pd.DataFrame(data)

def formatfunc(value, _): 
    return f"{int(value):,}"

fig, ax = plt.subplots(figsize=(25, 6))
counts = sns.barplot(x=df['countries'], y=df['cases'], data=df, label="Cases", ax=ax)

plt.subplots_adjust(left=0.08, right=1)

counts.yaxis.set_major_formatter(FuncFormatter(formatfunc))

for container in counts.containers: 
    counts.bar_label(container, fmt="%d", label_type="edge")

plt.show()