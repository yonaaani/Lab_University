import pandas as pd
import warnings
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.decomposition import PCA
from sklearn.svm import SVC
from sklearn.pipeline import Pipeline
from sklearn.metrics import classification_report, accuracy_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier

warnings.filterwarnings("ignore")

# Завантаження даних (замініть 'your_dataset.csv' на шлях до вашого датасету)
data = pd.read_csv('NetflixShows.csv')

data = pd.get_dummies(data, columns=['title', 'rating'], drop_first=True)
# Видалення дублікатів
data = data.drop_duplicates()
# Обробка відсутніх даних, заповнення середніми значеннями
data['user rating score'].fillna(data['user rating score'].mean(), inplace=True)
# Кодування категоріальних ознак (one-hot encoding)
data = pd.get_dummies(data, columns=['ratingLevel'])

# Розділення на навчальний та тестовий набори
X = data.drop('ratingDescription', axis=1)  # Означте 'target_column' як вашу цільову змінну
y = data['ratingDescription']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Створення конвейєра
pipeline = Pipeline([
    ('scaler', StandardScaler()),  # Нормалізація даних
    ('pca', PCA(n_components=0.95)),  # PCA з вибором компонент, які зберігають 95% дисперсії
    ('svm', SVC()),  # Модель Support Vector Machine
])

# Тренування моделі
pipeline.fit(X_train, y_train)

# Прогноз на тестовому наборі
y_pred = pipeline.predict(X_test)

# Оцінка моделі
accuracy = accuracy_score(y_test, y_pred)
classification_rep = classification_report(y_test, y_pred)

print("Перший конвеєр: ")

print(f"Accuracy: {accuracy}")
print("Classification Report:")
print(classification_rep)

print("\n")

# Створення конвейєра
pipeline = Pipeline([
    ('scaler', StandardScaler()),  # Нормалізація даних
    ('knn', KNeighborsClassifier()),  # Модель K Nearest Neighbors
])

# Тренування моделі
pipeline.fit(X_train, y_train)

# Прогноз на тестовому наборі
y_pred = pipeline.predict(X_test)

# Оцінка моделі
accuracy = accuracy_score(y_test, y_pred)
classification_rep = classification_report(y_test, y_pred)

print("Другий конвеєр: ")

print(f"Accuracy: {accuracy}")
print("Classification Report:")
print(classification_rep)

print("\n")

# Створення конвейєра
pipeline = Pipeline([
    ('minmax_scaler', MinMaxScaler()),  # Мінімакс нормалізація даних
    ('standard_scaler', StandardScaler()),  # Стандартизація даних
    ('decision_tree', DecisionTreeClassifier()),  # Модель Decision Tree
])

# Тренування моделі
pipeline.fit(X_train, y_train)

# Прогноз на тестовому наборі
y_pred = pipeline.predict(X_test)

# Оцінка моделі
accuracy = accuracy_score(y_test, y_pred)
classification_rep = classification_report(y_test, y_pred)

print("Третій конвеєр: ")

print(f"Accuracy: {accuracy}")
print("Classification Report:")
print(classification_rep)

print("\n")

# Створення конвейєра
pipeline = Pipeline([
    ('scaler', StandardScaler()),  # Нормалізація даних
    ('pca', PCA(n_components=0.95)),  # PCA з вибором компонент, які зберігають 95% дисперсії
    ('random_forest', RandomForestClassifier()),  # Модель Random Forest
])

# Тренування моделі
pipeline.fit(X_train, y_train)

# Прогноз на тестовому наборі
y_pred = pipeline.predict(X_test)

# Оцінка моделі
accuracy = accuracy_score(y_test, y_pred)
classification_rep = classification_report(y_test, y_pred)

print("Четвертий конвеєр: ")

print(f"Accuracy: {accuracy}")
print("Classification Report:")
print(classification_rep)

print("\n")
