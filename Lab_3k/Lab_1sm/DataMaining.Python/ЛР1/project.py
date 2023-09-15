import pandas as pd #для підключення csv
import numpy as np #для розрахунків
import matplotlib.pyplot as plt #для графіків

import seaborn as sns

#1. Завантажте власні дані. Для прикладу створимо фіктивний набір даних.
boba = pd.read_csv('NetflixShows.csv')
boba.head()

#2. Проведіть обрахунок описової статистики для аналізованих даних.
new_boba = boba.copy()
descriptive_stats = boba.describe()
print("Описова статистика:\n", descriptive_stats)

#3. Визначення та видалення рядків з пропущеними значеннями.
new_boba.dropna(inplace=True)

#4. Заміна пропущених значень на середнє значення по масиву.
mean_rating = new_boba['ratingDescription'].mean()
new_boba['ratingDescription'].fillna(mean_rating, inplace=True)
new_boba.to_csv('new_boba.csv', index=False)

#5. Заміна деяких елементів(перших трьох) на NaN.
if new_boba['rating'].isnull().any():
    print("Пропущені дані вже є в масиві")
else:
    # Замініть деякі елементи на NaN (наприклад, перші три елементи)
    new_boba.loc[0:2, 'rating'] = np.nan

# Повторіть попередній пункт для заміни значень R на NaN, якщо вони ще не NaN
new_boba_NaN = new_boba.copy()  # Створимо копію початкового DataFrame
new_boba_NaN['rating'] = new_boba_NaN['rating'].where(new_boba_NaN['rating'].isna(), np.nan)

#6. Визначте наявність «викидів» та приберіть їх з досліджуваного масиву (за допомогою функції boxplot або термокарт). У випадку їх відсутності – діяти аналогічно попередньому пункту.
# Створіть графік ящика з вусами для візуальної оцінки наявності викидів
sns.boxplot(x=new_boba['user rating score'])
plt.show()

# Визначте квантилі для визначення викидів
Q1 = new_boba['user rating score'].quantile(0.25)
Q3 = new_boba['user rating score'].quantile(0.75)
IQR = Q3 - Q1

# Додаю викиди, оскільки їх немає
new_boba.at[0, 'user rating score'] = 1
new_boba.at[10, 'user rating score'] = 10
new_boba.at[20, 'user rating score'] = 12
new_boba.at[30, 'user rating score'] = 25
new_boba.at[40, 'user rating score'] = 5
new_boba.at[50, 'user rating score'] = 7
sns.boxplot(x=new_boba['user rating score'])
plt.show()

# Визначте верхню та нижню межі для викидів
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

# Видаліть викиди
new_boba = new_boba[(new_boba['user rating score'] >= lower_bound) & (new_boba['user rating score'] <= upper_bound)]
sns.boxplot(x=new_boba['user rating score'], color='#eab676')
plt.show()

#7. Перерахуйте показники описової статистики для отриманого масиву.
descriptive_stats = new_boba.describe()
print("Кінцева описова статистика:\n", descriptive_stats)

#8. Проведіть операції центрування (від кожного елементу масиву відняти середнє значення) та нормування (кожен елемент масиву ділиться на середнє квадратичне відхилення) даних та перевірте результати операцій за рахунок обчислення дисперсії та суми всіх елементів отриманих масивів.
# Обчисліть середнє значення та стандартне відхилення
mean_value = np.mean(new_boba)
std_deviation = np.std(new_boba)

# Нормуйте дані (кожен елемент ділиться на стандартне відхилення)
normalized_boba = (new_boba - mean_value) / std_deviation

# Обчисліть дисперсію та суму елементів отриманого масиву
variance = np.var(normalized_boba)
sum_elements = np.sum(normalized_boba)

print("Нормовані дані:", normalized_boba)
print("Дисперсія:", variance)
print("Сума елементів:", sum_elements)