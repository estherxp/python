import seaborn as sns
import matplotlib.pyplot as plt

titanic = sns.load_dataset('titanic')
print(titanic.head())

# Cria o gráfico
sns.displot(x = 'class', y = 'age', data = titanic)
plt.show()