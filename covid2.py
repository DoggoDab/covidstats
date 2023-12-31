import matplotlib.pyplot as plt 
import pandas as pd 
import seaborn as sns 

sns.set()

year = ['2020', '2021', '2022', '2023']
casesWorld = [84301719, 293476267, 665949311, 700261811]
curedWorld = [67995032, 263678506, 637490164, 671449947]


data = {
    "year": year,
    "cases": casesWorld,
    "cured": curedWorld,
}

df = pd.DataFrame(data)

sns.lineplot(x=df['year'], y=df['cases'], color='black')
sns.lineplot(x=df['year'], y=df['cured'], color='lime')

plt.show()

