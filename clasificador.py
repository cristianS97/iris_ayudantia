from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import SGDClassifier
from sklearn.metrics import accuracy_score, classification_report
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import pickle
from pathlib import Path

ruta = Path(__file__).resolve().parent

iris = load_iris()

print(iris.keys())
print(type(iris))
print(iris.DESCR)

x, y = iris['data'], iris['target']

print(x.shape, y.shape)

print(y)
print(iris['target_names'])

print(iris.target_names[y])

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25, random_state=33)

print(x_train.shape, y_train.shape)
print(x_test.shape, y_test.shape)

df = pd.DataFrame(x_train, columns=iris['feature_names'])
sns.boxplot(data=df)
plt.xticks(rotation=90)

scaler = StandardScaler()

scaler.fit(x_train)

x_train = scaler.transform(x_train)
x_test = scaler.transform(x_test)

df2 = pd.DataFrame(x_train, columns=iris['feature_names'])
sns.boxplot(data=df2)
plt.xticks(rotation=90)

clf = SGDClassifier(max_iter=15, tol=None)
clf.fit(x_train, y_train)

print(clf.coef_)
print(clf.intercept_)

y_train_pred = clf.predict(x_train)
print(accuracy_score(y_train, y_train_pred))

y_pred = clf.predict(x_test)
print(accuracy_score(y_test, y_pred))

print(classification_report(y_test, y_pred, target_names=iris['target_names']))

print(x_test)
print(clf.predict(x_test))

print(iris['target_names'][clf.predict([[3, 3, 3, 3]])[0]])

with open(ruta.joinpath('clasificador.pkl'), 'wb') as f:
    pickle.dump(clf, f, pickle.HIGHEST_PROTOCOL)

with open(ruta.joinpath('clasificador.pkl'), 'rb') as f:
    new_clf = pickle.load(f)

print(iris['target_names'][new_clf.predict([[3, 3, 3, 3]])[0]])

