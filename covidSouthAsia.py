import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns 
from matplotlib.ticker import FuncFormatter 

sns.set()

dataCountries = ["Afghanistan", "Pakistan", "India", "Bhutan", "Bangladesh", "Nepal", "Sri Lanka", "Maldives"]
dataCases = [230403, 1581936, 45009660, 62697, 2046207, 1003450, 672685, 186694]

data = {
    "countries": dataCountries, 
    "cases": dataCases 
}

df = pd.DataFrame(data)

def formatfunc(value, _): 
    return f"{int(value):,}"

plt.figure(figsize=(10, 6))
counts = sns.barplot(x=df["countries"], y=df["cases"], data=df, label="Cases")

counts.yaxis.set_major_formatter(FuncFormatter(formatfunc))

for container in counts.containers: 
    counts.bar_label(container, fmt="%d", label_type="edge")

plt.show()