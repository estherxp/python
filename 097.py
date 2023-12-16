import seaborn as sns
import matplotlib.pyplot as plt

titanic = sns.load_dataset('titanic')
print(titanic.head())

sns.boxplot(x = 'class', y = 'age', data = titanic)
plt.show()