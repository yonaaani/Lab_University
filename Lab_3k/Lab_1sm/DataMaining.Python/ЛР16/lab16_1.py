import pandas as pd
import numpy as np
import warnings
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import VotingClassifier
from sklearn.ensemble import StackingClassifier
from sklearn.model_selection import GridSearchCV
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.neighbors import KNeighborsClassifier

warnings.filterwarnings("ignore")

# 1-2. Завантаження даних (замініть 'your_dataset.csv' на шлях до вашого датасету)
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

# 3. Сформуйте гомогенні ансамблі на основі будь-яких 2-х одиночних моделей (з попередніх робіт). Один з них зробіть паралельним, а інший - послідовним. Порівняйте ефективність роботи одиночних та ансамблевих моделей. 

# Одиничні моделі
model_rf = RandomForestClassifier(n_estimators=100, random_state=42)
model_logreg = LogisticRegression()

# Тренуємо моделі
model_rf.fit(X_train, y_train)
model_logreg.fit(X_train, y_train)

# Передбачення для тестового набору
y_pred_rf = model_rf.predict(X_test)
y_pred_logreg = model_logreg.predict(X_test)

# Оцінка точності для кожної моделі
accuracy_rf = accuracy_score(y_test, y_pred_rf)
accuracy_logreg = accuracy_score(y_test, y_pred_logreg)

print("Одиночні моделі:")

# Виведення точності на екран
print(f'Accuracy for Random Forest: {accuracy_rf}')
print(f'Accuracy for Logistic Regression: {accuracy_logreg}')

print("\n")

# Паралельний ансамбль
parallel_ensemble = VotingClassifier(estimators=[('rf', model_rf), ('logreg', model_logreg)], voting='hard')

# Тренуємо паралельний ансамбль
parallel_ensemble.fit(X_train, y_train)

# Оцінка ефективності паралельного ансамблю
y_pred_parallel_ensemble = parallel_ensemble.predict(X_test)
accuracy_parallel_ensemble = accuracy_score(y_test, y_pred_parallel_ensemble)

print("Паралельний ансамбль:")

print(f'Accuracy Parallel Ensemble: {accuracy_parallel_ensemble}')

print("\n")

# Послідовний ансамбль
sequential_ensemble = StackingClassifier(
    estimators=[('rf', model_rf), ('logreg', model_logreg)],
    final_estimator=LogisticRegression()
)

# Тренуємо послідовний ансамбль
sequential_ensemble.fit(X_train, y_train)

# Оцінка ефективності послідовного ансамблю
y_pred_sequential_ensemble = sequential_ensemble.predict(X_test)
accuracy_sequential_ensemble = accuracy_score(y_test, y_pred_sequential_ensemble)

print("Послідовний ансамбль:")

print(f'Accuracy Sequential Ensemble: {accuracy_sequential_ensemble}')

print("\n")

# 4. Для паралельного застосуйте почергово будь-які 2 підходи інтеграції прогнозів отриманих на основі базових моделей (1 простий і 1 складний зі слайду 21).

# Паралельний ансамбль
parallel_ensemble = VotingClassifier(estimators=[('rf', model_rf), ('logreg', model_logreg)], voting='soft')

# Тренуємо паралельний ансамбль
parallel_ensemble.fit(X_train, y_train)

# Отримуємо прогнози для базових моделей
probas = [model.predict_proba(X_test) for model in [model_rf, model_logreg]]

# Простий підхід: середнє значення ймовірностей
simple_integration = np.mean(probas, axis=0)

# Отримуємо прогнози з простого підходу
y_pred_simple_integration = np.argmax(simple_integration, axis=1)
accuracy_simple_integration = accuracy_score(y_test, y_pred_simple_integration)

print(f'Accuracy Simple Integration: {accuracy_simple_integration}')

# Виведення прогнозів для простого підходу
print("Predictions for Simple Integration:")
print(simple_integration)

print("\n")

# Метамодель для складного підходу
meta_model = LogisticRegression()

# Отримуємо прогнози для базових моделей
probas = [model.predict_proba(X_test) for model in [model_rf, model_logreg]]

# Збираємо прогнози в один масив
stacked_probas = np.hstack(probas)

# Тренуємо метамодель на прогнозах базових моделей
meta_model.fit(stacked_probas, y_test)

# Складний підхід: використання Logistic Regression як метамоделі
complex_integration = meta_model.predict_proba(stacked_probas)

# Отримуємо прогнози зі складного підходу
y_pred_complex_integration = np.argmax(complex_integration, axis=1)
accuracy_complex_integration = accuracy_score(y_test, y_pred_complex_integration)

print(f'Accuracy Complex Integration: {accuracy_complex_integration}')

# Виведення прогнозів для складного підходу
print("Predictions for Complex Integration:")
print(complex_integration)

print("\n")

# 5. Підберіть оптимальні параметри для створених ансамблевих моделей.

# Параметри для підбору
param_grid_parallel = {
    'rf__n_estimators': [50, 100, 200],
    'logreg__C': [0.1, 1, 10]
}

# Паралельний ансамбль
parallel_ensemble = VotingClassifier(estimators=[('rf', model_rf), ('logreg', model_logreg)], voting='soft')

# Grid Search для підбору оптимальних параметрів
grid_search_parallel = GridSearchCV(parallel_ensemble, param_grid_parallel, cv=5)
grid_search_parallel.fit(X_train, y_train)

# Отримані оптимальні параметри для паралельного ансамблю
best_params_parallel = grid_search_parallel.best_params_

print("Best parameters for parallel ensemble:", best_params_parallel)

print("\n")

# Параметри для підбору
param_grid_sequential = {
    'final_estimator__C': [0.1, 1, 10]
}

# Послідовний ансамбль
sequential_ensemble = StackingClassifier(
    estimators=[('rf', model_rf), ('logreg', model_logreg)],
    final_estimator=LogisticRegression()
)

# Grid Search для підбору оптимальних параметрів
grid_search_sequential = GridSearchCV(sequential_ensemble, param_grid_sequential, cv=5)
grid_search_sequential.fit(X_train, y_train)

# Отримані оптимальні параметри для послідовного ансамблю
best_params_sequential = grid_search_sequential.best_params_

print("Best parameters for sequential ensemble:", best_params_sequential)

print("\n")

# 6. Отримайте узагальнені показники важливості кожного з досліджуваних предикторів та інтерпретуйте отримані дані.

# Одинична модель Random Forest
model_rf = RandomForestClassifier(n_estimators=100, random_state=42)

# Тренуємо модель
model_rf.fit(X_train, y_train)

# Отримуємо показники важливості ознак
feature_importances_rf = model_rf.feature_importances_

# Створюємо DataFrame для відображення важливості ознак
feature_importance_df_rf = pd.DataFrame({'Feature': X_train.columns, 'Importance_RF': feature_importances_rf})

# Сортуємо за важливістю
feature_importance_df_rf = feature_importance_df_rf.sort_values(by='Importance_RF', ascending=False)

# Виводимо графік важливості ознак для Random Forest
plt.figure(figsize=(12, 6))
sns.barplot(x='Importance_RF', y='Feature', data=feature_importance_df_rf)
plt.title('Feature Importance - Random Forest')
plt.show()

# Одинична модель Logistic Regression
model_logreg = LogisticRegression()

# Тренуємо модель
model_logreg.fit(X_train, y_train)

# Отримуємо коефіцієнти важливості ознак
coefficients_logreg = model_logreg.coef_[0]

# Створюємо DataFrame для відображення важливості ознак
feature_importance_df_logreg = pd.DataFrame({'Feature': X_train.columns, 'Coefficient_LogReg': coefficients_logreg})

# Сортуємо за важливістю
feature_importance_df_logreg = feature_importance_df_logreg.sort_values(by='Coefficient_LogReg', ascending=False)

# Виводимо графік важливості ознак для Logistic Regression
plt.figure(figsize=(12, 6))
sns.barplot(x='Coefficient_LogReg', y='Feature', data=feature_importance_df_logreg)
plt.title('Feature Importance - Logistic Regression')
plt.show()

# 7. Розробіть та реалізуйте n-рівневий гомогенний ансамбль (де n>2) з застосуванням різних підходів формування ансамблів.

# Моделі на першому рівні
model_rf = RandomForestClassifier(n_estimators=100, random_state=42)
model_gb = GradientBoostingClassifier(n_estimators=100, random_state=42)

# Тренуємо моделі на першому рівні
model_rf.fit(X_train, y_train)
model_gb.fit(X_train, y_train)

# Прогнози моделей на першому рівні
y_pred_rf = model_rf.predict(X_test)
y_pred_gb = model_gb.predict(X_test)

# Моделі на другому рівні
model_logreg = LogisticRegression()
model_knn = KNeighborsClassifier()

# Тренуємо моделі на другому рівні
model_logreg.fit(X_train, y_train)
model_knn.fit(X_train, y_train)

# Прогнози моделей на другому рівні
y_pred_logreg = model_logreg.predict(X_test)
y_pred_knn = model_knn.predict(X_test)

# Моделі на третьому рівні (Voting Classifier)
model_voting = VotingClassifier(estimators=[
    ('rf', model_rf),
    ('gb', model_gb),
    ('logreg', model_logreg),
    ('knn', model_knn)
], voting='hard')

# Тренуємо Voting Classifier на третьому рівні
model_voting.fit(X_train, y_train)

# Прогноз Voting Classifier на третьому рівні
y_pred_voting = model_voting.predict(X_test)

# Визначення точності для моделей на першому та другому рівнях
accuracy_rf = accuracy_score(y_test, y_pred_rf)
accuracy_gb = accuracy_score(y_test, y_pred_gb)
accuracy_logreg = accuracy_score(y_test, y_pred_logreg)
accuracy_knn = accuracy_score(y_test, y_pred_knn)

# Визначення точності для моделі на третьому рівні
accuracy_voting = accuracy_score(y_test, y_pred_voting)

# Виведення точностей
print("Гомогенний ансамбль(4-ьох рівневий):")
print(f'Accuracy for RF: {accuracy_rf}')
print(f'Accuracy for GB: {accuracy_gb}')
print(f'Accuracy for Logistic Regression: {accuracy_logreg}')
print(f'Accuracy for KNN: {accuracy_knn}')
print(f'Accuracy for Voting: {accuracy_voting}')
