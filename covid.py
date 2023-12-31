import matplotlib.pyplot as plt 
import numpy as np 
import seaborn as sns 

sns.set()

con = np.array(['Asia', 'Europe', 'Africa', 'North America', 'South America', 'Oceania'])
cases = np.array([221084682, 252275920, 12856833, 129958009, 69396100, 14690713])

sns.catplot(x=cases, y=con, kind='violin')
plt.show()