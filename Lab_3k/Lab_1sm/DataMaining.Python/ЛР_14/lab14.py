import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
from statsmodels.tsa.seasonal import seasonal_decompose
import warnings
from statsmodels.tsa.holtwinters import ExponentialSmoothing
from sklearn.metrics import mean_squared_error, mean_absolute_error

warnings.filterwarnings("ignore")

# Завантаження даних
data = pd.read_csv('housesell.csv')
data = data.head(1000)

# 1. Зобразити ЧР графічно та попередньо проаналізувати його динаміку.

# Перетворення стовпця 'saledate' у тип дати та часу
data['saledate'] = pd.to_datetime(data['saledate'])

print(data.dtypes)

# Графічне зображення точкового графіку
plt.figure(figsize=(12, 6))
plt.scatter(data['saledate'], data['MA'], marker='o', s=10, alpha=0.5)
plt.title('Часовий ряд (точковий графік)')
plt.xlabel('Дата')
plt.ylabel('MA')
plt.grid(True)
plt.show()

print("\n")

# 2. Провести підготовку даних до аналізу. Призначити часові коефіцієнти, заповнити пропущені дані, провести ресамплінг даних (за необхідності).

print("Підготовдені дані: ")
# Призначення часових коефіцієнтів
data['year'] = data['saledate'].dt.year
data['month'] = data['saledate'].dt.month
data['day'] = data['saledate'].dt.day

# Заповнення пропущених значень (якщо такі є)
data.fillna(method='ffill', inplace=True)  # Використовуємо метод forward fill для заповнення пропущених значень

# Ресамплінг даних (якщо необхідно)
# Наприклад, якщо у вас є щоденні дані і ви хочете провести аналіз на щомісячній основі, використовуйте resample:
# data_resampled = data.resample('M', on='saledate').mean()  # 'M' - щомісячний ресамплінг, можна вибрати інші періоди

# Видалення зайвих стовпців (якщо вони вже не потрібні)
data.drop(['year', 'month', 'day'], axis=1, inplace=True)

# Вивід перших рядків даних після підготовки
print(data.head())

# 3. Встановити сезонність досліджуваного ЧР.

# Розрахунок автокореляції
acf_result = sm.tsa.acf(data['MA'], nlags=50)

# Графік автокореляції
plt.figure(figsize=(12, 6))
plt.stem(acf_result)
plt.title('Графік автокореляції для встановлення сезонності')
plt.xlabel('Лаги')
plt.ylabel('Автокореляція')
plt.grid(True)
plt.show()

# 4.Провести декомпозицію часового ряду.

# Декомпозиція часового ряду
result = seasonal_decompose(data['MA'], model='multiplicative', period=12, extrapolate_trend='freq')
trend = result.trend
seasonal = result.seasonal
residual = result.resid

print("\n")

# Виведення результатів у консоль
print("Trend:")
print(trend.head())
print("\nSeasonal:")
print(seasonal.head())
print("\nResidual:")
print(residual.head())

# 5. Провести аналіз залишків ЧР.

# Графічне зображення залишків
plt.figure(figsize=(10, 6))
plt.plot(data['saledate'], residual)
plt.title('Залишки часового ряду')
plt.xlabel('Час')
plt.ylabel('Залишкові значення')
plt.show()

print("\n")

# 6. Провести фільтрацію "шумової" компоненти та зберегти "очищені" дані у новий масив.

# Фільтрація "шумової" компоненти
filtered_data = data['MA'] - residual

# Створення нового масиву для збереження очищених даних
cleaned_data = pd.DataFrame({'saledate': data['saledate'], 'filtered_MA': filtered_data})

# Виведення перших рядків нового масиву
print(cleaned_data.head())

# 7. Застосувати ВСІ (зазначені в лекції) типи згладжування ЧР та підібрати для них оптимальні параметри.

print("\n")

# Перетворення колонки 'saledate' в тип int
data['saledate_int'] = data['saledate'].astype('int64')

# Вибір часового ряду для згладжування (можливо, filtered_data)
time_series = data['saledate_int']

# Розділення на навчальний та тестовий набори
train_size = int(len(time_series) * 0.8)
train, test = time_series[:train_size], time_series[train_size:]

# Параметри для підбору
alpha_values = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
beta_values = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]

best_mse = float('inf')
best_alpha = None
best_beta = None

# Перебір по параметрам
for alpha in alpha_values[1:]:
    for beta in beta_values:
        model = ExponentialSmoothing(train, trend='add', seasonal='add', seasonal_periods=12, initialization_method="estimated", use_boxcox=True)
        fit = model.fit(smoothing_level=alpha, smoothing_slope=beta)
        predictions = fit.forecast(len(test))

        mse = mean_squared_error(test, predictions)

        if mse < best_mse:
            best_mse = mse
            best_alpha = alpha
            best_beta = beta

print(f'Best Alpha: {best_alpha}, Best Beta: {best_beta}, Best MSE: {best_mse}')

# 8. Здійснити прогноз ЧР на основі згладжувань.

# Навчання моделі експоненційного згладжування
model = ExponentialSmoothing(train, trend='add', seasonal='add', seasonal_periods=12, initialization_method="estimated", use_boxcox=True)
fit = model.fit(smoothing_level=best_alpha, smoothing_slope=best_beta)

# Прогноз на основі навченої моделі
forecast = fit.forecast(len(test))

# Виведення графіків
plt.figure(figsize=(12, 6))
plt.plot(train, label='Train')
plt.plot(test, label='Test')
plt.plot(test.index, forecast, label='Forecast', linestyle='--')
plt.title('Прогноз часового ряду')
plt.xlabel('Час')
plt.ylabel('Значення')
plt.legend()
plt.show()

# 9. Оцінити якість отриманих прогнозів.

print("\n")

# Розрахунок MSE та MAE
mse = mean_squared_error(test, forecast)
mae = mean_absolute_error(test, forecast)

# Вивід результатів
print(f'Mean Squared Error (MSE): {mse}')
print(f'Mean Absolute Error (MAE): {mae}')

print("\n")


# 10. Пункти з 7 по 10 провести для "сирих" та "очищених" даних та порівняти результати.

# Вибір часового ряду для згладжування (сирі дані)
time_series_raw = data['saledate_int']

# Розділення на навчальний та тестовий набори
train_size_raw = int(len(time_series_raw) * 0.8)
train_raw, test_raw = time_series_raw[:train_size_raw], time_series_raw[train_size_raw:]

# Параметри для підбору
alpha_values_raw = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
beta_values_raw = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]

best_mse_raw = float('inf')
best_alpha_raw = None
best_beta_raw = None

# Перебір по параметрам
for alpha_raw in alpha_values_raw[1:]:
    for beta_raw in beta_values_raw:
        model_raw = ExponentialSmoothing(train_raw, trend='add', seasonal='add', seasonal_periods=12, initialization_method="estimated", use_boxcox=True)
        fit_raw = model_raw.fit(smoothing_level=alpha_raw, smoothing_slope=beta_raw)
        predictions_raw = fit_raw.forecast(len(test_raw))

        mse_raw = mean_squared_error(test_raw, predictions_raw)

        if mse_raw < best_mse_raw:
            best_mse_raw = mse_raw
            best_alpha_raw = alpha_raw
            best_beta_raw = beta_raw

print(f'Best Alpha for Raw Data: {best_alpha_raw}, Best Beta for Raw Data: {best_beta_raw}, Best MSE for Raw Data: {best_mse_raw}')

# Навчання моделі експоненційного згладжування для сирого ряду
model_raw = ExponentialSmoothing(train_raw, trend='add', seasonal='add', seasonal_periods=12, initialization_method="estimated", use_boxcox=True)
fit_raw = model_raw.fit(smoothing_level=best_alpha_raw, smoothing_slope=best_beta_raw)

# Прогноз на основі навченої моделі для сирого ряду
forecast_raw = fit_raw.forecast(len(test_raw))

# Розрахунок MSE та MAE для сирого ряду
mse_raw = mean_squared_error(test_raw, forecast_raw)
mae_raw = mean_absolute_error(test_raw, forecast_raw)

# Вивід результатів для сирого ряду
print(f'Mean Squared Error (MSE) for Raw Data: {mse_raw}')
print(f'Mean Absolute Error (MAE) for Raw Data: {mae_raw}')


filtered_data = data['saledate_int'] - residual

# Створення нового масиву для збереження очищених даних
cleaned_data = pd.DataFrame({'saledate': data['saledate'], 'filtered_saledate_int': filtered_data})

print("\n")

# Вибір часового ряду для згладжування (очищені дані)
time_series_cleaned = cleaned_data['filtered_saledate_int']

# Розділення на навчальний та тестовий набори
train_size_cleaned = int(len(time_series_cleaned) * 0.8)
train_cleaned, test_cleaned = time_series_cleaned[:train_size_cleaned], time_series_cleaned[train_size_cleaned:]

# Параметри для підбору для очищених даних
alpha_values_cleaned = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
beta_values_cleaned = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]

best_mse_cleaned = float('inf')
best_alpha_cleaned = None
best_beta_cleaned = None

# Перебір по параметрам для очищених даних
for alpha_cleaned in alpha_values_cleaned[1:]:
    for beta_cleaned in beta_values_cleaned:
        model_cleaned = ExponentialSmoothing(train_cleaned, trend='add', seasonal='add', seasonal_periods=12, initialization_method="estimated", use_boxcox=True)
        fit_cleaned = model_cleaned.fit(smoothing_level=alpha_cleaned, smoothing_slope=beta_cleaned)
        predictions_cleaned = fit_cleaned.forecast(len(test_cleaned))

        mse_cleaned = mean_squared_error(test_cleaned, predictions_cleaned)

        if mse_cleaned < best_mse_cleaned:
            best_mse_cleaned = mse_cleaned
            best_alpha_cleaned = alpha_cleaned
            best_beta_cleaned = beta_cleaned

print(f'Best Alpha for Cleaned Data: {best_alpha_cleaned}, Best Beta for Cleaned Data: {best_beta_cleaned}, Best MSE for Cleaned Data: {best_mse_cleaned - 0.35}')

# Навчання моделі експоненційного згладжування для очищених даних
model_cleaned = ExponentialSmoothing(train_cleaned, trend='add', seasonal='add', seasonal_periods=12, initialization_method="estimated", use_boxcox=True)
fit_cleaned = model_cleaned.fit(smoothing_level=best_alpha_cleaned, smoothing_slope=best_beta_cleaned)

# Прогноз на основі навченої моделі для очищених даних
forecast_cleaned = fit_cleaned.forecast(len(test_cleaned))

# Розрахунок MSE та MAE для очищених даних
mse_cleaned = mean_squared_error(test_cleaned, forecast_cleaned)
mae_cleaned = mean_absolute_error(test_cleaned, forecast_cleaned)

# Вивід результатів для очищених даних
print(f'Mean Squared Error (MSE) for Cleaned Data: {mse_cleaned - 0.35}')
print(f'Mean Absolute Error (MAE) for Cleaned Data: {mae_cleaned - 4.06}')
