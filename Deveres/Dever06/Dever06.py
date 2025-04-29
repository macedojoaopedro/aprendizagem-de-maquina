from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

iris = load_iris()
X, y = iris.data, iris.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

modelo = KNeighborsClassifier(n_neighbors=3)
modelo.fit(X_train, y_train)

print("Digite os dados da flor:")

a = float(input("Comprimento da sépala: "))
b = float(input("Largura da sépala: "))
c = float(input("Comprimento da pétala: "))
d = float(input("Largura da pétala: "))

res = modelo.predict([[a, b, c, d]])

print("Tipo de flor:", iris.target_names[res[0]])

