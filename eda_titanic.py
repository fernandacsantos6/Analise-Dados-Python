import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Carregar dataset
url = 'https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv'
df = pd.read_csv(url)

# Mostrar as primeiras linhas
print(df.head())

# Informações básicas
print(df.info())

# Estatísticas descritivas
print(df.describe())

# Visualização: sobreviventes por sexo
sns.countplot(x='Survived', hue='Sex', data=df)
plt.title('Sobreviventes por Sexo')
plt.show()

# Visualização: distribuição de idade
sns.histplot(df['Age'].dropna(), bins=30, kde=True)
plt.title('Distribuição de Idade')
plt.show()
 
