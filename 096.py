import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

titanic = sns.load_dataset('titanic')
print(titanic.head())

sns.histplot(titanic['fare'], kde=True, bins = 30)
plt.show()