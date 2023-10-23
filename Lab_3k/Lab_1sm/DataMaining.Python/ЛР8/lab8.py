import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.model_selection import GridSearchCV, RandomizedSearchCV
from sklearn.model_selection import ShuffleSplit, LeaveOneOut, StratifiedShuffleSplit, GroupShuffleSplit
import numpy as np

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

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=90)
groups = np.arange(len(X_train))

print("Shape of X_train:", X_train[['user rating score', 'release year']].shape)
print("Shape of y_train:", y_train.shape)
print("Shape of groups:", groups.shape)

# Побудуйте SVM-модель і навчіть її на навчальних даних
svm_model = SVC(kernel='linear')  # Змінено тип ядра на 'linear'
svm_model.fit(X_train[['user rating score', 'release year']], y_train)  # Використовуйте лише 2 ознаки для навчання

# Отримайте передбачення для тестових даних
y_pred = svm_model.predict(X_test[['user rating score', 'release year']])

# 1. Підбір параметрів моделі на основі відкладеної та відкладеної валідаційної вибірки
# Вибірка з перемішуванням
shuffle_split = ShuffleSplit(n_splits=3, test_size=0.2, random_state=0)

# Вибірка Leave one out
loo = LeaveOneOut()

# Стратифікована вибірка з перемішуванням
strat_shuffle_split = StratifiedShuffleSplit(n_splits=3, test_size=0.2, random_state=0)

# Групова вибірка з перемішуванням
group_shuffle_split = GroupShuffleSplit(n_splits=3, test_size=0.2, random_state=0)

# 2. Підбір параметрів з усіма стратегіями
param_grid = {'C': [1], 'gamma': [1], 'kernel': ['linear', 'rbf']}
grid_search_shuffle = GridSearchCV(SVC(), param_grid, cv=shuffle_split)
grid_search_shuffle.fit(X_train[['user rating score', 'release year']], y_train)
print("Best parameters found on Shuffle Split using Grid Search:", grid_search_shuffle.best_params_)

grid_search_loo = GridSearchCV(SVC(), param_grid, cv=loo)
grid_search_loo.fit(X_train[['user rating score', 'release year']], y_train)
print("Best parameters found on Leave One Out using Grid Search:", grid_search_loo.best_params_)

grid_search_strat = GridSearchCV(SVC(), param_grid, cv=strat_shuffle_split)
grid_search_strat.fit(X_train[['user rating score', 'release year']], y_train)
print("Best parameters found on Stratified Shuffle Split using Grid Search:", grid_search_strat.best_params_)


grid_search_group = GridSearchCV(SVC(), param_grid, cv=group_shuffle_split)
grid_search_group.fit(X_train[['user rating score', 'release year']], y_train, groups=groups)
print("Best parameters found on Group Shuffle Split using Grid Search:", grid_search_group.best_params_)

print("\n")

# 4. Випадковий пошук параметрів
random_param_grid = {'C': [0.1, 1, 10], 'gamma': [0.1, 1, 10], 'kernel': ['linear', 'rbf']}
random_search_shuffle = RandomizedSearchCV(SVC(), random_param_grid, n_iter=3, cv=shuffle_split, random_state=0)
random_search_shuffle.fit(X_train[['user rating score', 'release year']], y_train)
print("Best parameters found on Shuffle Split using Random Search:", random_search_shuffle.best_params_)

random_search_loo = RandomizedSearchCV(SVC(), random_param_grid, n_iter=3, cv=loo, random_state=0)
random_search_loo.fit(X_train[['user rating score', 'release year']], y_train)
print("Best parameters found on Leave One Out using Random Search:", random_search_loo.best_params_)

random_search_strat = RandomizedSearchCV(SVC(), random_param_grid, n_iter=3, cv=strat_shuffle_split, random_state=0)
random_search_strat.fit(X_train[['user rating score', 'release year']], y_train)
print("Best parameters found on Stratified Shuffle Split using Random Search:", random_search_strat.best_params_)

random_search_group = RandomizedSearchCV(SVC(), random_param_grid, n_iter=3, cv=group_shuffle_split, random_state=0)
random_search_group.fit(X_train[['user rating score', 'release year']], y_train, groups=groups)
print("Best parameters found on Group Shuffle Split using Random Search:", random_search_group.best_params_)

