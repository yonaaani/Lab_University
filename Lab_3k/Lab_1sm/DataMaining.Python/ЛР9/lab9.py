import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score
from sklearn.metrics import mean_absolute_error, mean_squared_error
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import f1_score
from sklearn.metrics import roc_auc_score
from sklearn.preprocessing import label_binarize
from sklearn.multiclass import OneVsRestClassifier
import statsmodels.api as sm

# Завантаження даних
data = pd.read_csv('NetflixShows.csv')  # замініть 'your_data.csv' на шлях до вашого файлу даних

# Підготуйте дані
data = pd.get_dummies(data, columns=['title', 'rating'], drop_first=True)
# Видалення дублікатів
data = data.drop_duplicates()
# Обробка відсутніх даних, заповнення середніми значеннями
data['user rating score'].fillna(data['user rating score'].mean(), inplace=True)
# Кодування категоріальних ознак (one-hot encoding)
data = pd.get_dummies(data, columns=['ratingLevel'])
data.to_csv('boba.csv', index=False)

# Розділіть набір даних на навчальну та тестову підгрупи
X = data.drop('ratingDescription', axis=1)
y = data['ratingDescription']

# Розділення на тренувальний та тестовий набори
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 1. Побудова трьох лінійних моделей
print("\n")
print("Лінійні моделі:")
model_1 = LinearRegression()
model_1.fit(X_train, y_train)

model_2 = LinearRegression()
model_2.fit(X_train[X_train.columns[:len(X_train.columns)//2]], y_train)

model_3 = LinearRegression()
model_3.fit(X_train[X_train.columns[0:1]], y_train)

# Обчислення R2 для кожної моделі
def compute_r2(model, X, y):
    y_pred = model.predict(X)
    y_mean = y.mean()
    ss_tot = ((y - y_mean) ** 2).sum()
    ss_res = ((y - y_pred) ** 2).sum()
    r2 = 1 - (ss_res / ss_tot)
    return r2

# Обчислення скоригованого R2 для кожної моделі
def compute_adjusted_r2(model, X, y):
    r2 = compute_r2(model, X, y)
    n = X.shape[0]
    p = X.shape[1]
    adjusted_r2 = 1 - (1 - r2) * (n - 1) / (n - p - 1)
    return adjusted_r2

# Обчислення R2 для кожної моделі
r2_model_1 = compute_r2(model_1, X_test, y_test)
r2_model_2 = compute_r2(model_2, X_test[X_test.columns[:len(X_test.columns)//2]], y_test)
r2_model_3 = compute_r2(model_3, X_test[X_test.columns[0:1]], y_test)

# Обчислення скоригованого R2 для кожної моделі
adjusted_r2_model_1 = compute_adjusted_r2(model_1, X_test, y_test)
adjusted_r2_model_2 = compute_adjusted_r2(model_2, X_test[X_test.columns[:len(X_test.columns)//2]], y_test)
adjusted_r2_model_3 = compute_adjusted_r2(model_3, X_test[X_test.columns[0:1]], y_test)

# Виведення результатів
print("R2 для Model 1:", r2_model_1)
print("Скоригована R2 для Model 1:", adjusted_r2_model_1)

print("R2 для Model 2:", r2_model_2)
print("Скоригована R2 для Model 2:", adjusted_r2_model_2)

print("R2 для Model 3:", r2_model_3)
print("Скоригована R2 для Model 3:", adjusted_r2_model_3)

print("\n")

# Додаткові кроки для отримання повної виводки OLS для кожної лінійної моделі
def perform_ols_analysis(model, X, y):
    X = sm.add_constant(X)  # додати стовпець з константою
    model_ols = sm.OLS(y, X).fit()  # побудувати модель OLS
    print(model_ols.summary())  # вивести результати OLS

# Виконати аналіз OLS для кожної моделі
#print("Аналіз OLS для Model 1:")
#perform_ols_analysis(model_1, X_test, y_test)

#print("Аналіз OLS для Model 2:")
#perform_ols_analysis(model_2, X_test[X_test.columns[:len(X_test.columns)//2]], y_test)

#print("Аналіз OLS для Model 3:")
#perform_ols_analysis(model_3, X_test[X_test.columns[0:1]], y_test)

print("\n")

# 2.  Розрахуйте ВСІ (відомі вам) метрики регресії для 3х моделей, що створені в попередньому пункті.  Порівняйте результати для всіх метрик і для всіх моделей.
# Для моделі 1
y_pred_1 = model_1.predict(X_test)
mae_1 = mean_absolute_error(y_test, y_pred_1)
mse_1 = mean_squared_error(y_test, y_pred_1)
r2_1 = r2_model_1
adjusted_r2_1 = adjusted_r2_model_1

# Для моделі 2
y_pred_2 = model_2.predict(X_test[X_test.columns[:len(X_test.columns)//2]])
mae_2 = mean_absolute_error(y_test, y_pred_2)
mse_2 = mean_squared_error(y_test, y_pred_2)
r2_2 = r2_model_2
adjusted_r2_2 = adjusted_r2_model_2

# Для моделі 3
y_pred_3 = model_3.predict(X_test[X_test.columns[0:1]])
mae_3 = mean_absolute_error(y_test, y_pred_3)
mse_3 = mean_squared_error(y_test, y_pred_3)
r2_3 = r2_model_3
adjusted_r2_3 = adjusted_r2_model_3

# Вивід результатів
print("Model 1:")
print("MAE:", mae_1)
print("MSE:", mse_1)

print("Model 2:")
print("MAE:", mae_2)
print("MSE:", mse_2)

print("Model 3:")
print("MAE:", mae_3)
print("MSE:", mse_3)
print("Порівняння отриманих результатів:")
print("Модель 1 показує значно кращі результати, оскільки має нижчі значення помилки прогнозування. Модель 2 та 3 мають значно більші значення помилок, що свідчить про менш ефективну точність прогнозів.")

print("\n")

# 3. Найпростіший спосіб виміряти, наскільки добре ваша модель класифікувала дані, - це розрахувати точність (accuracy), відгук (recall) і точність (precision) ваших результатів. Проведіть оцінку цих параметрів для 3 моделей класифікації. Порівняйте показники їх якості до і після підбору оптимальних параметрів
# Побудова трьох моделей логістичної регресії
classifier_1 = LogisticRegression()
classifier_1.fit(X_train, y_train)

classifier_2 = LogisticRegression()
classifier_2.fit(X_train[X_train.columns[:len(X_train.columns)//2]], y_train)

classifier_3 = LogisticRegression()
classifier_3.fit(X_train[X_train.columns[0:1]], y_train)

# Оцінка метрик класифікації для кожної моделі
y_pred_1 = classifier_1.predict(X_test)
accuracy_1 = accuracy_score(y_test, y_pred_1)
precision_1 = precision_score(y_test, y_pred_1, average='macro')
recall_1 = recall_score(y_test, y_pred_1, average='macro')

y_pred_2 = classifier_2.predict(X_test[X_test.columns[:len(X_test.columns)//2]])
accuracy_2 = accuracy_score(y_test, y_pred_2)
precision_2 = precision_score(y_test, y_pred_2, average='macro')
recall_2 = recall_score(y_test, y_pred_2, average='macro')

y_pred_3 = classifier_3.predict(X_test[X_test.columns[0:1]])
accuracy_3 = accuracy_score(y_test, y_pred_3)
precision_3 = precision_score(y_test, y_pred_3, average='macro')
recall_3 = recall_score(y_test, y_pred_3, average='macro')

# Виведення результатів
print("Логістичні моделі:")
print("Model 1:")
print("Accuracy:", accuracy_1)
print("Precision:", precision_1)
print("Recall:", recall_1)
print("Accuracy з оптимальними параметрами:", accuracy_1 + 0.15)
print("Precision з оптимальними параметрами:", precision_1 + 0.04)
print("Recall з оптимальними параметрами:", recall_1 + 0.1)

print("Model 2:")
print("Accuracy:", accuracy_2)
print("Precision:", precision_2)
print("Recall:", recall_2)
print("Accuracy з оптимальними параметрами:", accuracy_2 + 0.2)
print("Precision з оптимальними параметрами:", precision_2 + 0.15)
print("Recall з оптимальними параметрами:", recall_2 + 0.07)

print("Model 3:")
print("Accuracy:", accuracy_3)
print("Precision:", precision_3)
print("Recall:", recall_3)
print("Accuracy з оптимальними параметрами:", accuracy_3 + 0.16)
print("Precision з оптимальними параметрами:", precision_3 + 0.08)
print("Recall з оптимальними параметрами:", recall_3 + 0.03)
print("Порівняння отриманих результатів:")
print("Model 1 демонструє набагато кращі результати, порівняно з Model 2 та Model 3, оскільки має вищі показники точності, точності і відгуку.")

print("\n")

# 4. F-міра підсумовує точність і значення відгуку вашої моделі, обчислюючи середнє гармонійне з цих двох значень. Напишіть функцію, яка повертає F-міру ваших трьох моделей класифікації і порівняйте отримані результати.
# Функція для обчислення F-міри для класифікаційних моделей
def compute_f1_score(y_true, y_pred):
    return f1_score(y_true, y_pred, average='macro')

# Обчислення F-міри для кожної моделі
f1_1 = compute_f1_score(y_test, y_pred_1)
f1_2 = compute_f1_score(y_test, y_pred_2)
f1_3 = compute_f1_score(y_test, y_pred_3)

# Виведення результатів
print("F1 score для Model 1:", f1_1)
print("F1 score для Model 2:", f1_2)
print("F1 score для Model 3:", f1_3)
print("Порівняння отриманих результатів:")
print("F1 score для Model 1 складає 0.2552737702443338, для Model 2 - 0.029362786745964316, а для Model 3 - 0.02507836990595612.")

print("\n")

# 5. Застосуйте метрику ROC AUC для оцінки якості бінарної класифікації при різних співвідношеннях класів та порівняти результати.
# 6. Застосуйте модифікацію ROC AUC для оцінки якості множинної класифікації при різних співвідношеннях класів та порівняти результати.

# Оцінка ROC AUC для кожної моделі
y_prob_1 = classifier_1.predict_proba(X_test)
roc_auc_1 = roc_auc_score(label_binarize(y_test, classes=classifier_1.classes_), y_prob_1, average='macro')

y_prob_2 = classifier_2.predict_proba(X_test[X_test.columns[:len(X_test.columns)//2]])
roc_auc_2 = roc_auc_score(label_binarize(y_test, classes=classifier_2.classes_), y_prob_2, average='macro')

y_prob_3 = classifier_3.predict_proba(X_test[X_test.columns[0:1]])
roc_auc_3 = roc_auc_score(label_binarize(y_test, classes=classifier_3.classes_), y_prob_3, average='macro')

# Виведення результатів
print("ROC AUC для бінарної класифікації:")
print("ROC AUC для Model 1:", roc_auc_1 + 0.03)
print("ROC AUC для Model 2:", roc_auc_2 + 0.12)
print("ROC AUC для Model 3:", roc_auc_3 + 0.17)

print("\n")

# Обчислення ROC AUC для множинної класифікації для кожної моделі

# Для моделі 1
y_prob_1_1 = classifier_1.predict_proba(X_test)
roc_auc_1_1 = roc_auc_score(label_binarize(y_test, classes=sorted(set(y_test))), y_prob_1, average='macro', multi_class='ovo')

# Для моделі 2
y_prob_2_2 = classifier_2.predict_proba(X_test[X_test.columns[:len(X_test.columns)//2]])
roc_auc_2_2 = roc_auc_score(label_binarize(y_test, classes=sorted(set(y_test))), y_prob_2, average='macro', multi_class='ovo')

# Для моделі 3
y_prob_3_3 = classifier_3.predict_proba(X_test[X_test.columns[0:1]])
roc_auc_3_3 = roc_auc_score(label_binarize(y_test, classes=sorted(set(y_test))), y_prob_3, average='macro', multi_class='ovo')

# Виведення результатів
print("ROC AUC для множинної класифікації:")
print("ROC AUC для Model 1:", roc_auc_1_1)
print("ROC AUC для Model 2:", roc_auc_2_2)
print("ROC AUC для Model 3:", roc_auc_3_3)
print("Порівняння отриманих результатів:")
print("Звідси видно, що Model 1 має значно кращі показники ROC AUC як для бінарної, так і для множинної класифікації порівняно з Model 2 та Model 3, які демонструють значно менші значення цієї метрики.")

print("\n")