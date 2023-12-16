import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

titanic = sns.load_dataset('titanic')
dados = titanic.sex.value_counts()
etiquetas = ['male', 'female']

sns.barplot(x=etiquetas, y=dados, color='orange')
plt.show()