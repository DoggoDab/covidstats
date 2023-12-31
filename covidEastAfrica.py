import matplotlib.pyplot as plt 
import pandas as pd 
import seaborn as sns 
from matplotlib.ticker import FuncFormatter 

sns.set()

dataCountries = ["Djibouti", "Eritrea", "Madagascar", "Mauritius", "Rwanda", "South \nSudan", "Sudan", "Tanzania", "Seychelles", "Comoros", "Ethiopia", "Somalia", "Kenya", "Uganda"]
dataCases = [15690, 10189, 68436, 43025, 133518, 18765, 63993, 43223, 51220, 9109, 501117, 27334, 344130, 171983]

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