import pandas as pd
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.model_selection import GridSearchCV

# Завантаження вашого набору даних
boba = pd.read_csv('NetflixShows.csv')

# Підготовка даних
boba.dropna(inplace=True)
boba = pd.get_dummies(boba, columns=['title', 'rating'], drop_first=True)
boba = boba.drop_duplicates()
boba['user rating score'].fillna(boba['user rating score'].mean(), inplace=True)
boba_encoded = pd.get_dummies(boba, columns=['ratingLevel'])
boba_encoded.to_csv('boba.csv', index=False)

# Розбиття на тренувальну та тестову вибірки
X = boba_encoded.drop('ratingDescription', axis=1)
y = boba_encoded['ratingDescription']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Бінарна класифікація
try:
    binary_model = LogisticRegression(max_iter=1000)
    binary_model.fit(X_train, y_train)
except KeyboardInterrupt:
    pass

binary_predictions = binary_model.predict(X_test)
binary_accuracy = accuracy_score(y_test, binary_predictions)

param_grid_binary = {'penalty': ['l1', 'l2'], 'C': [0.01, 0.1], 'solver': ['liblinear', 'saga']}
grid_search_binary = GridSearchCV(estimator=binary_model, param_grid=param_grid_binary, scoring='accuracy', cv=5)
grid_search_binary.fit(X_train, y_train)
best_params_binary = grid_search_binary.best_params_
optimal_binary_model = LogisticRegression(penalty=best_params_binary['penalty'], C=best_params_binary['C'], solver=best_params_binary['solver'])
optimal_binary_model.fit(X_train, y_train)
binary_accuracy_optimal = accuracy_score(y_test, optimal_binary_model.predict(X_test))

# Множинна класифікація
try:
    multi_class_model = LogisticRegression(multi_class='multinomial', solver='lbfgs', max_iter=1000)
    multi_class_model.fit(X_train, y_train)
except KeyboardInterrupt:
    pass

multi_class_predictions = multi_class_model.predict(X_test)
multi_class_accuracy = accuracy_score(y_test, multi_class_predictions)

param_grid_multi = {'penalty': ['l1', 'l2'], 'C': [0.01, 0.1], 'solver': ['saga', 'lbfgs']}
grid_search_multi = GridSearchCV(estimator=multi_class_model, param_grid=param_grid_multi, scoring='accuracy', cv=5)
grid_search_multi.fit(X_train, y_train)
best_params_multi = grid_search_multi.best_params_
optimal_multi_class_model = LogisticRegression(multi_class='multinomial', penalty=best_params_multi['penalty'], C=best_params_multi['C'], solver=best_params_multi['solver'])
optimal_multi_class_model.fit(X_train, y_train)
multi_class_accuracy_optimal = accuracy_score(y_test, optimal_multi_class_model.predict(X_test))

print("\n")
# Виведення результатів
print(f"Точність бінарної моделі: {binary_accuracy}")
print(f"Точність оптимальної бінарної моделі: {binary_accuracy_optimal}")
print(f"Точність моделі з багатьма класами: {multi_class_accuracy}")
print(f"Точність оптимальної моделі з багатьма класами: {multi_class_accuracy_optimal}")

# Перехресна перевірка для обох моделей
scores_binary = cross_val_score(optimal_binary_model, X, y, cv=5, scoring='accuracy')
print(f"Середня точність за допомогою перехресної перевірки для бінарної класифікації: {scores_binary.mean()}")
print(f"Стандартне відхилення за допомогою перехресної перевірки для бінарної класифікації: {scores_binary.std()}")

scores_multi = cross_val_score(optimal_multi_class_model, X, y, cv=5, scoring='accuracy')
print(f"Середня точність за допомогою перехресної перевірки для множинної класифікації: {scores_multi.mean()}")
print(f"Стандартне відхилення за допомогою перехресної перевірки для множинної класифікації: {scores_multi.std()}")
print("\n")
