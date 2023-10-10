import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report  # Додайте цей рядок
from sklearn.model_selection import GridSearchCV
import matplotlib.pyplot as plt


# 1. Завантажте ваш набір даних
boba = pd.read_csv('NetflixShows.csv')

# 2. Підготуйте дані
boba.dropna(inplace=True)
boba = pd.get_dummies(boba, columns=['title', 'rating'], drop_first=True)
# Видалення дублікатів
boba = boba.drop_duplicates()
# Обробка відсутніх даних, заповнення середніми значеннями
boba['user rating score'].fillna(boba['user rating score'].mean(), inplace=True)
# Кодування категоріальних ознак (one-hot encoding)
boba = pd.get_dummies(boba, columns=['ratingLevel'])

# 3. Розділіть набір даних на навчальну та тестову підгрупи
X = boba.drop('ratingDescription', axis=1)
y = boba['ratingDescription']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=90)

# 4-5. Створення моделі k-NN
knn_classifier = KNeighborsClassifier()

# Параметри для перебору
param_grid = {
    'n_neighbors': [3, 5, 7, 9],  # Перебирайте різні кількості сусідів
    'metric': ['euclidean', 'manhattan'],  # Перебирайте різні метрики відстані
}

# Пошук оптимальних параметрів за допомогою перехресної перевірки
grid_search = GridSearchCV(knn_classifier, param_grid, cv=5, scoring='accuracy')
grid_search.fit(X_train, y_train)

best_knn = grid_search.best_estimator_
y_pred = best_knn.predict(X_test)
y_pred_best = best_knn.predict(X_test)

# Створіть класифікаційну модель на основі k-NN з початковими параметрами
knn_initial = KNeighborsClassifier()
knn_initial.fit(X_train, y_train)
y_pred_initial = knn_initial.predict(X_test)

# Найкращі параметри
best_params = grid_search.best_params_
print("Оптимальні параметри:", best_params)

# Виміряйте точність для обох моделей
accuracy_best = accuracy_score(y_test, y_pred_best)
accuracy_initial = accuracy_score(y_test, y_pred_initial)

print("\n")
# Виведіть результати
print("Точність для моделі з початковими параметрами:", accuracy_initial)
print("Точність для моделі з оптимальними параметрами:", accuracy_best)

# Розрахуйте та відобразіть матрицю плутанини та звіт про класифікацію для моделі з оптимальними параметрами
conf_matrix_best = confusion_matrix(y_test, y_pred_best)
class_report_best = classification_report(y_test, y_pred_best)

print("\nМатриця плутанини для моделі з оптимальними параметрами:\n", conf_matrix_best)
print("\nЗвіт про класифікацію для моделі з оптимальними параметрами:\n", class_report_best)

# Розрахуйте та відобразіть матрицю плутанини та звіт про класифікацію для моделі з початковими параметрами
conf_matrix_initial = confusion_matrix(y_test, y_pred_initial)
class_report_initial = classification_report(y_test, y_pred_initial)

print("\nМатриця плутанини для моделі з початковими параметрами:\n", conf_matrix_initial)
print("\nЗвіт про класифікацію для моделі з початковими параметрами:\n", class_report_initial)

# 7-8. Оцініть параметри "оптимальної" моделі
# Порівняйте гіперпараметри початкової та оптимальної моделей, щоб побачити, як вони змінилися
initial_knn = KNeighborsClassifier()  # Ініціалізувати новий класифікатор K-NN
initial_knn.fit(X_train, y_train)  # Підгоніть початкову модель без налаштування гіперпараметрів

print("\nПараметри початкової моделі:")
print("Кількість сусідів:", initial_knn.n_neighbors)
print("Схема ваги:", initial_knn.weights)
print("Параметр степеня (p):", initial_knn.p)

print("\nПараметри оптимальної моделі:")
print("Кількість сусідів (Оптимально):", best_knn.n_neighbors)
print("Схема ваги (Оптимально):", best_knn.weights)
print("Параметр степеня (p) (Оптимально):", best_knn.p)
print("\n")