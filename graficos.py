import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# importação

gorjeta = sns.load_dataset('tips')

# mostar o inicio

print(gorjeta.head())

# plotagem de distribuição univariada (Histogramas)
sns.histplot(gorjeta['total_bill'], kde=True, bins = 30)

# plotagem comparada
sns.jointplot(x = 'total_bill', y = 'tip', data=gorjeta)

sns.jointplot(x = 'total_bill', y = 'tip', data=gorjeta, kind='hex')

sns.jointplot(x = 'total_bill', y = 'tip', data=gorjeta, kind='reg')

# grafico de dispensão para todas as variaveis numéricas
sns.pairplot(gorjeta)

# seleção combinada
sns.pairplot(gorjeta, hue = 'sex')

# plotagem de categorias
sns.barplot(x = 'sex', y = 'total_bill', data=gorjeta)
sns.barplot(x = 'sex', y = 'total_bill', data=gorjeta, estimator=np.std)

# exibir o grafico
plt.show()


