import pandas as pd
import warnings
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report
from mlxtend.classifier import EnsembleVoteClassifier
from sklearn.ensemble import VotingClassifier
from mlxtend.classifier import StackingClassifier
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.ensemble import GradientBoostingClassifier

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

# 3. Сформуйте паралельний гетерогенний ансамбль
# Одиночні моделі
rf_clf = RandomForestClassifier(random_state=42)
svm_clf = SVC(random_state=42)
lr_clf = LogisticRegression(random_state=42)
dt_clf = DecisionTreeClassifier(random_state=42)

print("Одиничні моделі: ")

# Порівняння ефективності одиночних моделей
for clf, label in zip([rf_clf, svm_clf, lr_clf, dt_clf], ['Random Forest', 'SVM', 'Logistic Regression', 'Decision Tree']):
    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f"{label} Accuracy: {accuracy}")

# Оцінка інших показників (precision, recall, f1-score)
for clf, label in zip([rf_clf, svm_clf, lr_clf, dt_clf], ['Random Forest', 'SVM', 'Logistic Regression', 'Decision Tree']):
    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)
    report = classification_report(y_test, y_pred)
    print(f"{label} Classification Report:\n{report}")
    
print("\n")

print("Ансамбль з чотирьох одиночних моделей: ")

# Ансамбль з чотирьох одиночних моделей
ensemble_clf = EnsembleVoteClassifier(clfs=[rf_clf, svm_clf, lr_clf, dt_clf], voting='hard')

# Порівняння ефективності одиночних та ансамблевої моделей
for clf, label in zip([rf_clf, svm_clf, lr_clf, dt_clf, ensemble_clf], ['Random Forest', 'SVM', 'Logistic Regression', 'Decision Tree', 'Ensemble']):
    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f"{label} Accuracy: {accuracy}")
    
print("\n")

# 4. Застосуйте почергово будь-які 2 підходи інтеграції прогнозів отриманих на основі базових моделей (1 простий і 1 складний зі слайду 21).

# Простий блендінг (голосування)
simple_blend_clf = VotingClassifier(estimators=[('rf', rf_clf), ('svm', svm_clf), ('lr', lr_clf), ('dt', dt_clf)], voting='hard')

# Тренування
simple_blend_clf.fit(X_train, y_train)

# Прогноз
simple_blend_pred = simple_blend_clf.predict(X_test)

# Оцінка точності
simple_blend_accuracy = accuracy_score(y_test, simple_blend_pred)
print(f"Simple Blending Accuracy: {simple_blend_accuracy}")

print("\n")

# Стекінг
stacking_clf = StackingClassifier(classifiers=[rf_clf, svm_clf, lr_clf, dt_clf], 
                                  meta_classifier=LogisticRegression(), 
                                  use_probas=False)

# Тренування
stacking_clf.fit(X_train, y_train)

# Прогноз
stacking_pred = stacking_clf.predict(X_test)

# Оцінка точності
stacking_accuracy = accuracy_score(y_test, stacking_pred)
print(f"Stacking Accuracy: {stacking_accuracy}")

print("\n")

# 5. Підберіть оптимальні параметри для створеної ансамблевої моделі.

# Створення EnsembleVoteClassifier
ensemble_clf = EnsembleVoteClassifier(clfs=[rf_clf, svm_clf, lr_clf, dt_clf], voting='hard')

# Оптимальні параметри для пошуку
param_grid = {
    'randomforestclassifier__n_estimators': [50, 100, 200],
    'svc__C': [0.1, 1, 10],
    'logisticregression__C': [0.1, 1, 10],
    'decisiontreeclassifier__max_depth': [None, 10, 20]
}

# Пошук оптимальних параметрів
grid = GridSearchCV(estimator=ensemble_clf, param_grid=param_grid, cv=3)
grid.fit(X_train, y_train)

# Отримання найкращих параметрів
best_params = grid.best_params_

# Створення EnsembleVoteClassifier з оптимальними параметрами
optimized_ensemble_clf = EnsembleVoteClassifier(clfs=[
    RandomForestClassifier(n_estimators=best_params['randomforestclassifier__n_estimators'], random_state=42),
    SVC(C=best_params['svc__C'], random_state=42),
    LogisticRegression(C=best_params['logisticregression__C'], random_state=42),
    DecisionTreeClassifier(max_depth=best_params['decisiontreeclassifier__max_depth'], random_state=42)
], voting='hard')

# Тренування на оптимальних параметрах
optimized_ensemble_clf.fit(X_train, y_train)

# Прогноз
y_pred_optimized = optimized_ensemble_clf.predict(X_test)

print("Optimal Parameters:")
print(f"Random Forest - n_estimators: {best_params['randomforestclassifier__n_estimators']}")
print(f"SVM - C: {best_params['svc__C']}")
print(f"Logistic Regression - C: {best_params['logisticregression__C']}")
print(f"Decision Tree - max_depth: {best_params['decisiontreeclassifier__max_depth']}")

# Оцінка точності
accuracy_optimized = accuracy_score(y_test, y_pred_optimized)
print(f"Optimized Ensemble Accuracy: {accuracy_optimized}")

print("\n")

# 6. Отримайте узагальнені показники важливості кожного з досліджуваних предикторів та інтерпретуйте отримані дані.

# Оцінка важливості функцій для Random Forest
rf_feature_importances = rf_clf.feature_importances_

# Оцінка важливості функцій для Decision Tree
dt_feature_importances = dt_clf.feature_importances_

# Загальна важливість функцій у ансамблевій моделі (середнє значення)
ensemble_feature_importances = (rf_feature_importances + dt_feature_importances) / 2

# Сортування індексів за значеннями важливості
sorted_indices = ensemble_feature_importances.argsort()[::-1]
    
# Створення DataFrame для відображення важливості функцій
importance_df = pd.DataFrame({
    'Feature': X.columns[sorted_indices],
    'Importance': ensemble_feature_importances[sorted_indices]
})

# Побудова графіка важливості функцій
plt.figure(figsize=(10, 6))
sns.barplot(x='Importance', y='Feature', data=importance_df, palette='viridis')
plt.title('Feature Importance in Ensemble Model')
plt.xlabel('Importance')
plt.ylabel('Feature')
plt.show()

# 7. Розробіть та реалізуйте n-рівневий гетерогенний ансамбль (де n>2) з застосуванням різних підходів формування ансамблів.

# Розділення на навчальний та тестовий набори
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Перший рівень ансамблю: RandomForest та GradientBoosting
rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
gb_model = GradientBoostingClassifier(n_estimators=100, random_state=42)

rf_model.fit(X_train, y_train)
gb_model.fit(X_train, y_train)

rf_predictions = rf_model.predict(X_test)
gb_predictions = gb_model.predict(X_test)

# Створення нового набору функцій для другого рівня ансамблю
new_features = pd.DataFrame({'RF_Predictions': rf_predictions, 'GB_Predictions': gb_predictions})

# Другий рівень ансамблю: Logistic Regression
lr_model = LogisticRegression()
lr_model.fit(new_features, y_test)

# Передбачення на тестовому наборі
final_predictions = lr_model.predict(new_features)

# Оцінка точності ансамблю
ensemble_accuracy = accuracy_score(y_test, final_predictions)
print(f"Ensemble Accuracy: {ensemble_accuracy}")

print("\n")

# 8. Сформуйте послідовний гетерогенний ансамбль на основі різних одиночних моделей (з попередніх робіт).  Порівняйте ефективність роботи одиночних та ансамблевої моделей. 

# Розділення на навчальний та тестовий набори
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Моделі першого рівня
rf_first_level = RandomForestClassifier(random_state=42)
svm_first_level = SVC(random_state=42)
lr_first_level = LogisticRegression(random_state=42)

# Тренування моделей першого рівня
rf_first_level.fit(X_train, y_train)
svm_first_level.fit(X_train, y_train)
lr_first_level.fit(X_train, y_train)

# Прогнози моделей першого рівня на тестовому наборі
rf_predictions = rf_first_level.predict(X_test)
svm_predictions = svm_first_level.predict(X_test)
lr_predictions = lr_first_level.predict(X_test)

# Створення нового набору даних для моделі другого рівня
second_level_data = pd.DataFrame({
    'RF_Prediction': rf_predictions,
    'SVM_Prediction': svm_predictions,
    'LR_Prediction': lr_predictions
})

# Модель другого рівня
second_level_model = GradientBoostingClassifier(random_state=42)

# Тренування моделі другого рівня на прогнозах першого рівня
second_level_model.fit(second_level_data, y_test)

# Прогноз моделі другого рівня
second_level_predictions = second_level_model.predict(second_level_data)

# Оцінка точності
accuracy_single_models = {
    'Random Forest': accuracy_score(y_test, rf_predictions),
    'SVM': accuracy_score(y_test, svm_predictions),
    'Logistic Regression': accuracy_score(y_test, lr_predictions),
}

accuracy_ensemble_model = accuracy_score(y_test, second_level_predictions)

# Виведення результатів
print("Accuracy of Single Models:")
for model, acc in accuracy_single_models.items():
    print(f"{model}: {acc}")

print("\nAccuracy of Ensemble Model:")
print(f"Sequential Ensemble: {accuracy_ensemble_model}")