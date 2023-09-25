# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 19:59:24 2023

@author: yonaaani
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.model_selection import GridSearchCV

#1. Завантажте ваш набір даних
boba = pd.read_csv('NetflixShows.csv')

#2. Підготуйте дані з використанням підходів з попередніх лабораторних робіт.

# Видалила дублікати
boba = boba.drop_duplicates()
# Обробрала відсутні дані, наприклад, заповнила середніми значеннями
boba['user rating score'].fillna(boba['user rating score'].mean(), inplace=True)
# Кодування категоріальних ознак (one-hot encoding)
boba = pd.get_dummies(boba, columns=['ratingLevel'])
boba.to_csv('good_boba.csv', index=False)

#3. Розбийте ваш набір даних на навчальну та тестові підгрупи з використанням всіх відомих вам підходів.

X = boba.drop('rating', axis=1)  
X = pd.get_dummies(boba.drop('rating', axis=1))
y = boba['rating']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=90)

#4. Отримайте дерева рішень, що міститиме набір вирішуючих правил для класифікації та прогнозу даних.

# Побудова моделі дерева рішень
clf = DecisionTreeClassifier()
clf.fit(X_train, y_train)


#5. Оцініть якість отриманої моделі (принаймні 2-ма способами). 

# Прогнози моделі на тестовому наборі даних
y_pred = clf.predict(X_test)
# Оцінка якості моделі на тестовому наборі даних
accuracy = accuracy_score(y_test, y_pred)
report = classification_report(y_test, y_pred)
conf_matrix = confusion_matrix(y_test, y_pred)
print("\n")
print("Точність:", accuracy)
print("Звіт про класифікацію:\n", report)
print("Матриця помилок(де саме):\n", conf_matrix)
print("\n")

#6. Підберіть оптимальні параметри моделі, зокрема, оптимальну складність.

# Параметри для оптимізації
param_grid = {'max_depth': [3, 5, 7], 'min_samples_split': [2, 5, 10]}
# Пошук оптимальних параметрів з використанням перехресної перевірки
grid_search = GridSearchCV(estimator=DecisionTreeClassifier(), param_grid=param_grid, cv=5)
grid_search.fit(X_train, y_train)
# Використовую GridSearchCV для пошуку оптимальних параметрів моделі.
best_params = grid_search.best_params_
print("Оптимальні параметри:", best_params)

#7. Виконайте обрізку та перебудову дерева, відповідно до параметрів, визначених у пункті 6.

# Оптимальні параметри
best_max_depth = best_params['max_depth']
best_min_samples_split = best_params['min_samples_split']
# Перебудова моделі з оптимальними параметрами
best_clf = DecisionTreeClassifier(max_depth=best_max_depth, min_samples_split=best_min_samples_split)
best_clf.fit(X_train, y_train)

#8. Оцініть параметри "оптимальної моделі". Які з них змінились? Як саме?

# Оцінка якості оптимальної моделі
y_best_pred = best_clf.predict(X_test)
best_accuracy = accuracy_score(y_test, y_best_pred)
best_report = classification_report(y_test, y_best_pred)
best_conf_matrix = confusion_matrix(y_test, y_best_pred)
print("Точність оптимальної моделі:", best_accuracy)
print("\n")
print("Звіт про класифікацію:\n", best_report)
print("Матриця помилок(де саме):\n", best_conf_matrix)
print("\n")

#9. Важливість ознак у моделі

print("Важливість ознак у моделі:")
# Створюємо список кортежів (ознака, важливість) для ненульових важливостей і сортуємо їх за важливістю у зворотньому порядку
feature_importance = [(column, importance) for column, importance in zip(X.columns, best_clf.feature_importances_) if importance > 0]
feature_importance_sorted = sorted(feature_importance, key=lambda x: x[1], reverse=True)
# Виводимо список ознак та їх важливості
for feature, importance in feature_importance_sorted:
    print(f"{feature}: {importance}")
print("\n")




