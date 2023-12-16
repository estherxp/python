import seaborn as sns
import matplotlib.pyplot as plt

titanic = sns.load_dataset('titanic')
print(titanic.head())

sns.jointplot(x = 'fare', y = 'age', data=titanic)
plt.show()