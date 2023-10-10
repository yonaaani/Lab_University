import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, confusion_matrix
from mlxtend.plotting import plot_decision_regions
from sklearn.model_selection import GridSearchCV

# Завантажте ваш набір даних
boba = pd.read_csv('NetflixShows.csv')

# Підготуйте дані
boba = pd.get_dummies(boba, columns=['title', 'rating'], drop_first=True)
# Видалення дублікатів
boba = boba.drop_duplicates()
# Обробка відсутніх даних, заповнення середніми значеннями
boba['user rating score'].fillna(boba['user rating score'].mean(), inplace=True)
# Кодування категоріальних ознак (one-hot encoding)
boba = pd.get_dummies(boba, columns=['ratingLevel'])
boba.to_csv('boba.csv', index=False)

# Розділіть набір даних на навчальну та тестову підгрупи
X = boba.drop('ratingDescription', axis=1)
y = boba['ratingDescription']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=90)

# Побудуйте SVM-модель і навчіть її на навчальних даних
svm_model = SVC(kernel='linear')  # Змінено тип ядра на 'linear'
svm_model.fit(X_train[['user rating score', 'release year']], y_train)  # Використовуйте лише 2 ознаки для навчання

# Отримайте передбачення для тестових даних
y_pred = svm_model.predict(X_test[['user rating score', 'release year']])


# Візуалізація моделі (спосіб 1 - розміщення на графіку)
plt.scatter(X_test['user rating score'], X_test['release year'], c=y_pred)
plt.xlabel('user rating score')
plt.ylabel('release year')
plt.title('Візуалізація SVM-моделі (спосіб 1)')
plt.show()

# Візуалізація моделі (спосіб 2 - використання графіку рішучої поверхні)
X_visualization = X_test[['user rating score', 'release year']]  # Отримайте дані для візуалізації
y_test = y_test.to_numpy()

plot_decision_regions(X_visualization.values, y_test, clf=svm_model, legend=2)
plt.xlabel('user rating score')
plt.ylabel('release year')
plt.title('Візуалізація SVM-моделі (спосіб 2)')
plt.show()

# Підбір оптимальних параметрів моделі (наприклад, через GridSearchCV)

param_grid = {'C': [0.1, 1, 10], 'kernel': ['linear', 'rbf', 'poly']}
grid_search = GridSearchCV(SVC(), param_grid, cv=5)
grid_search.fit(X_train, y_train)
best_svm_model = grid_search.best_estimator_

# Оцінимо якість оптимальної моделі на тестових даних
y_pred_optimal = best_svm_model.predict(X_test)
accuracy_optimal = accuracy_score(y_test, y_pred_optimal)
confusion_optimal = confusion_matrix(y_test, y_pred_optimal)

print("\n")
print(f"Accuracy of the optimal model: {accuracy_optimal}")
print("Confusion Matrix for the optimal model:")
print(confusion_optimal)

# Оцінка змінених параметрів оптимальної моделі
print("Параметри оптимальної моделі:")
print(best_svm_model.get_params())