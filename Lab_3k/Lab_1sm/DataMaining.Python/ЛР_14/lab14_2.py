import pandas as pd
import numpy as np 
import warnings
import matplotlib.pyplot as plt
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from statsmodels.tsa.statespace.sarimax import SARIMAX
from statsmodels.tsa.stattools import acf
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.ensemble import IsolationForest
import seaborn as sns
from sklearn.cluster import KMeans

warnings.filterwarnings("ignore")

# Зчитуємо дані
data = pd.read_csv('BreadBasket.csv')
data = data.head(1000)
data = data.dropna()
print(data.isna().sum())

data['Date'] = pd.to_datetime(data['Date'])
data['Time'] = pd.to_datetime(data['Time'])
data['Item'] = pd.Categorical(data['Item']) 
data['Transaction'] = data['Transaction'].astype(int)
label_encoder = LabelEncoder()
data['Item'] = label_encoder.fit_transform(data['Item'])

print(data.head())
print("\n")
print(data.dtypes)
print("\n")
print:(np.asarray(data))

# 1. Стаціонаризація часового ряду
# Наприклад, за допомогою диференціації
data['stationary'] = data['Date'].diff().dropna()

# 2. Графіки автокореляції та часткової автокореляції
plot_acf(data['Date'])
plot_pacf(data['Date'])
plt.show()

# 3. Побудова (S)AR(I)MA моделі
# Реалізуйте SARIMA модель за допомогою бібліотеки statsmodels

# Виберемо тільки числові стовпці
data_numeric = data.select_dtypes(include=[np.number])

# Продовжимо з моделлю SARIMAX
p, d, q = 1, 1, 1
P, D, Q, s = 1, 1, 1, 12
data_numeric_np = np.asarray(data_numeric)
print(data_numeric_np.shape)

endog_variable = data_numeric_np[:, data_numeric.columns.get_loc('Transaction')].astype(int)
endog_series = data_numeric_np[:, data_numeric.columns.get_loc('Transaction')].astype(float)

model = SARIMAX(endog_series, order=(p, d, q), seasonal_order=(P, D, Q, s))
results = model.fit()

print(results.summary())

# 4. Підібір оптимальних параметрів для моделі
# Використовуйте критерії, такі як AIC, BIC, для визначення оптимальних параметрів

print("\n")

# Виведіть статистики моделі та оцінки параметрів
print(results.summary())

# Оцінка моделі за критеріями AIC та BIC
print(f"AIC: {results.aic}")
print(f"BIC: {results.bic}")

print("\n")

# 5. Аналіз залишків моделі
# Вивчіть залишки на предмет їх адекватності

# Виведіть графік залишків та їх автокореляції
residuals = results.resid

# Plotting the residuals
plt.figure(figsize=(10, 6))
plt.plot(residuals)
plt.title('Residuals Value')
plt.xlabel('Observation')
plt.ylabel('Residual Value')
plt.show()

# Перевірка автокореляції залишків
acf_resid = acf(residuals, nlags=20)

# Plotting the ACF of residuals
plt.figure(figsize=(10, 6))
plt.stem(acf_resid)
plt.title('ACF of Residuals')
plt.xlabel('Lag')
plt.ylabel('ACF Value')
plt.show()

# 6. Побудова прогнозу з довірчими інтервалами
# Визначення кількості кроків для прогнозу
forecast_steps = 20  # You can adjust this value based on your needs

# Отримання прогнозу та довірчих інтервалів
forecast = results.get_forecast(steps=forecast_steps)
forecast_index = pd.date_range(start=data['Date'].max(), periods=forecast_steps + 1, freq='D')[1:]

# Виведення графіку прогнозу та довірчих інтервалів
plt.figure(figsize=(10, 6))
plt.plot(data['Date'], data['Transaction'], label='Observed')
plt.plot(forecast_index, forecast.predicted_mean, color='red', label='Forecast')
plt.fill_between(forecast_index, forecast.conf_int()[:, 0], forecast.conf_int()[:, 1], color='pink', alpha=0.3, label='Confidence Interval')
plt.title('Forecast with Confidence Intervals')
plt.xlabel('Date')
plt.ylabel('Transaction')
plt.legend()
plt.show()

# 7. Всі пункти перераховані вище (1-6) реалізувати для "сирих" та "очищених" даних та порівняти результати

print("\n")

print(" 7. Оскільки в мене датасет хороший, то дані одразу очищені і немає сенсу виводити і те і те, однаковий виходить результат, перевірила на перших пунктах(додам скріни)")

print("\n")

# 8. Провести класифікацію ЧР

# Підготовка даних
data['Class'] = np.where(data['Transaction'].diff() > 0, 'Increase', np.where(data['Transaction'].diff() < 0, 'Decrease', 'Stable'))
X = data[['Transaction']]  # Здебільшого тут буде більше функцій
y = data['Class']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Вибір та тренування моделі
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Прогнозування та оцінка результатів
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy: {accuracy}')

print("\n")

# 9. Визначити аномалії в досліджуваних ЧР

# Підготовка даних
X = data[['Transaction']]

# Вибір та тренування моделі
model = IsolationForest(contamination=0.05)  # Задання рівня забруднення (процент аномалій)
model.fit(X)

# Прогнозування аномалій
data['Anomaly'] = model.predict(X)

# Виведення аномальних значень
anomalies = data[data['Anomaly'] == -1]
print("Anomalies:")
print(anomalies)

# 10. Проаналізувати взаємодію між декількома ЧР, в багатомірному ЧР.

# Кореляційний аналіз:

# Розрахунок матриці кореляції

label_encoder = LabelEncoder()
data['Class'] = label_encoder.fit_transform(data['Class'])

correlation_matrix = data.corr()

sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=.5)
plt.show()

# Кластерний аналіз:
    
# Підготовка даних (X - ваші часові ряди)
X = data[['Transaction', 'Item']]

# Вибір та тренування моделі k-means
kmeans = KMeans(n_clusters=2)
data['Cluster'] = kmeans.fit_predict(X)

# Візуалізація кластерів
plt.scatter(X['Transaction'], X['Item'], c=data['Cluster'], cmap='viridis')
plt.xlabel('Transaction')
plt.ylabel('Item')
plt.show()

# Аналіз крос-кореляції:
    
# Приклад для обчислення крос-кореляції
lags = range(-10, 11)
cross_corr = [np.correlate(data['Transaction'].values, data['Item'].shift(shift).fillna(0).values) for shift in lags]

# Візуалізація крос-кореляції
plt.stem(lags, cross_corr)
plt.xlabel('Lag')
plt.ylabel('Cross-Correlation')
plt.show()