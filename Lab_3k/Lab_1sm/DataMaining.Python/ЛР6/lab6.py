import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Ridge, Lasso
from sklearn.model_selection import GridSearchCV
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score, mean_squared_error

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
boba.to_csv('boba.csv', index=False)

# 3. Розбиття на тренувальну та тестову вибірки
X = boba.drop('ratingDescription', axis=1)
y = boba['ratingDescription']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 4.Створіть прогнозну моделі для досліджуваних даних на основі лінійної регресії:
    
# З використанням одного Х
model_single = LinearRegression()
model_single.fit(X_train[['release year']], y_train)
print("Початкові параметри моделі з одним Х:")
print("Коефіцієнт: ", model_single.coef_)
print("Перехоплення: ", model_single.intercept_)
print("\n")

# З використанням кількох Х-ів
model_multiple = LinearRegression()
model_multiple.fit(X_train[['release year', 'user rating score', 'user rating size']], y_train)
print("Початкові параметри моделі з кількома Х:")
print("Коефіцієнти: ", model_multiple.coef_)
print("Перехоплення: ", model_multiple.intercept_)
print("\n")

# 5. Підіберіть оптимальні параметри створених моделей для досліджуваних даних (параметри регуляризації, гребенева та лассо регресія)
# Для Ridge регресії
ridge = Ridge()
param_grid = {'alpha': [0.1, 1, 10]}
grid_ridge = GridSearchCV(ridge, param_grid, cv=5)
grid_ridge.fit(X_train, y_train)
print("Оптимальні параметри для Ridge регресії:")
print("Найкращі параметри: ", grid_ridge.best_params_)
print("Найкращий результат (за оцінкою крос-валідації): ", grid_ridge.best_score_)
print("\n")

# Для Lasso регресії
lasso = Lasso()
param_grid = {'alpha': [0.1, 1, 10]}
grid_lasso = GridSearchCV(lasso, param_grid, cv=5)
grid_lasso.fit(X_train, y_train)
print("Оптимальні параметри для Lasso регресії:")
print("Найкращі параметри: ", grid_lasso.best_params_)
print("Найкращий результат (за оцінкою крос-валідації): ", grid_lasso.best_score_)
print("\n")

# 6. Візуалізуйте початкові та "оптимальні" моделі.

# Візуалізація початкової моделі з одним Х
plt.scatter(X_test['release year'], y_test, color='black', label='Actual Data')
plt.plot(X_test['release year'], model_single.predict(X_test[['release year']]), color='blue', linewidth=1, label='Initial Model')
plt.xlabel('Release Year')
plt.ylabel('Rating Description')
plt.title('Linear Regression Model with One Feature')
plt.legend()
plt.show()
plt.figure(figsize=(12, 6))

# Візуалізація оптимальної моделі з крос-валідацією для Ridge
plt.scatter(X_test['release year'], y_test, color='black', label='Actual Data')
plt.plot(X_test['release year'], grid_ridge.best_estimator_.predict(X_test), color='green', linewidth=1, label='Optimal Ridge Model')
plt.xlabel('Release Year')
plt.ylabel('Rating Description')
plt.title('Ridge Regression Model with Optimal Parameters')
plt.legend()
plt.show()
plt.figure(figsize=(12, 6))

# Візуалізація оптимальної моделі з крос-валідацією для Lasso
plt.scatter(X_test['release year'], y_test, color='black', label='Actual Data')
plt.plot(X_test['release year'], grid_lasso.best_estimator_.predict(X_test), color='red', linewidth=1, label='Optimal Lasso Model')
plt.xlabel('Release Year')
plt.ylabel('Rating Description')
plt.title('Lasso Regression Model with Optimal Parameters')
plt.legend()
plt.show()
plt.figure(figsize=(12, 6))

# Візуалізація початкової моделі з кількома Х-ів
plt.figure(figsize=(10, 6))
y_pred_multiple = model_multiple.predict(X_test[['release year', 'user rating score', 'user rating size']])
plt.scatter(X_test['release year'], y_test, color='black', label='Actual Data')
plt.plot(X_test['release year'], y_pred_multiple, color='red', linewidth=1, label='Initial Model with Multiple Features')
plt.xlabel('Release Year')
plt.ylabel('Rating Description')
plt.title('Linear Regression Model with Multiple Features')
plt.legend()
plt.show()
plt.figure(figsize=(12, 6))

# 7. Оцінка для початкових моделей
y_pred_single = model_single.predict(X_test[['release year']])
r2_single = r2_score(y_test, y_pred_single)
mse_single = mean_squared_error(y_test, y_pred_single)

y_pred_multiple = model_multiple.predict(X_test[['release year', 'user rating score', 'user rating size']])
r2_multiple = r2_score(y_test, y_pred_multiple)
mse_multiple = mean_squared_error(y_test, y_pred_multiple)

print("Оцінка для початкової моделі з одним Х:")
print("R2-оцінка: ", r2_single)
print("Середньоквадратична помилка (MSE): ", mse_single)

print("Оцінка для початкової моделі з кількома Х-ів:")
print("R2-оцінка: ", r2_multiple)
print("Середньоквадратична помилка (MSE): ", mse_multiple)

# Оцінка для моделі з оптимальним Ridge
y_pred_ridge = grid_ridge.best_estimator_.predict(X_test)
r2_ridge = r2_score(y_test, y_pred_ridge)
mse_ridge = mean_squared_error(y_test, y_pred_ridge)

# Оцінка для моделі з оптимальним Lasso
y_pred_lasso = grid_lasso.best_estimator_.predict(X_test)
r2_lasso = r2_score(y_test, y_pred_lasso)
mse_lasso = mean_squared_error(y_test, y_pred_lasso)

print("Оцінка для оптимальної моделі з Ridge регресією:")
print("R2-оцінка: ", r2_ridge)
print("Середньоквадратична помилка (MSE): ", mse_ridge)

print("Оцінка для оптимальної моделі з Lasso регресією:")
print("R2-оцінка: ", r2_lasso)
print("Середньоквадратична помилка (MSE): ", mse_lasso)