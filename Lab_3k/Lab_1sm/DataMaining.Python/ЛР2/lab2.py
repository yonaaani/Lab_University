# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 18:34:31 2023

@author: yonaaani
"""
import pandas as pd #для підключення csv
import numpy as np #для розрахунків
import matplotlib.pyplot as plt #для графіків
import scipy.stats as stats
from scipy.stats import shapiro
import seaborn as sns
from sklearn.preprocessing import LabelEncoder
from sklearn.impute import SimpleImputer

boba = pd.read_csv('NetflixShows.csv')
boba.head()
new_boba = boba.copy()

#1.Здійсніть групування даних за декількома змінними, що іллюструватиме певну закономірність для досліджуваних даних. При цьому, здійсніть сортування за однією зі змінних.

# Згрупувала дані за стовпцями 'ratingLevel' і 'release year', обчислюючи середнє значення рейтингу
grouped_data = new_boba.groupby(['title', 'release year'])['ratingDescription'].mean().reset_index()
grouped_data.to_csv('grouped_data.csv', index=False)

# Сортування за однією змінною (наприклад, вибрала за 'title')
sorted_data = grouped_data.sort_values(by='title', ascending=True)
sorted_data.to_csv('sorted_data.csv', index=False)

#2.Створіть таблицю співпряженості для будь-яких двох змінних (з врахуванням їх типу) так, щоб отримана таблиця іллюструвала певну закономірність для досліджуваних даних.

# Створення таблиці співпряженості
contingency_table = pd.crosstab(new_boba['rating'], new_boba['title'])
contingency_table.to_csv('contingency_table.csv', index=False)

#3. Встановити нормальність розподілу для ознак в вашому наборі даних (усіма запропонованими способами). До тих ознак, розподіл яких не є нормальним застосувати техніки приведення розподілу до нормального та візуалізувати результати до та після.

columns_to_drop = ['title', 'rating','ratingLevel']
df = pd.DataFrame(new_boba)
df = df.drop(columns=columns_to_drop)

# Перевірка нормальності за допомогою тесту Шапіро-Уілка
stat, p = shapiro(df)

# p-value менше 0.05 вказує на відхилення від нормального розподілу
if p > 0.05:
    print("Розподіл є нормальним.")
    # Припустимо, що ваш DataFrame називається df
    df['ratingDescription'].hist(color='#9bc2a5')
    plt.xlabel('Rating Description')
    plt.ylabel('Frequency')
    plt.title('Histogram of Rating Description')
    plt.show()
    
    # Графік гістограми
    df['release year'].hist(color='#9bc2a5')
    plt.xlabel('Release Year')
    plt.ylabel('Frequency')
    plt.title('Histogram of Release Year')
    plt.show()
    
    # Графік розкиду (scatter plot)
    plt.scatter(df.index, df['release year'], color='#f2ec91')
    plt.xlabel('Index')
    plt.ylabel('Release Year')
    plt.title('Scatter Plot of Release Year')
    plt.show()
    
    df['user rating score'].hist(color='#9bc2a5')
    plt.xlabel('User Rating Score')
    plt.ylabel('Frequency')
    plt.title('Histogram of User Rating Score')
    plt.show()
    
    df['user rating size'].hist(color='#9bc2a5')
    plt.xlabel('User Rating Size')
    plt.ylabel('Frequency')
    plt.title('Histogram of User Rating Size')
    plt.show()
    
else:
    print("Розподіл не є нормальним.")
    # Логарифмування даних
    log_data = np.log(new_boba)
    
    # Візуалізація гістограми та Q-Q графіку після логарифмування
    plt.hist(log_data, bins=5, density=True, alpha=0.6, color='b')
    stats.probplot(log_data, dist="norm", plot=plt)
    plt.show()
    
#4. Знайти кореляції (краще через візуалізацію) між усіма ознаками у датасеті та на основі цього обгрунтувати  доцільність їх подальшого використання.

# Обчисліть матрицю кореляцій
correlation_matrix = new_boba.corr()

# Створіть теплокарту кореляцій за допомогою Seaborn
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)
plt.title('Correlation Heatmap')
plt.show()

#5. Спробуйте себе у feature engineering: здійсніть перетворення одних типів даних в інші (категоріальних у числові і навпаки), здійсніть відбір значущих ознак та конструювання нових. Обгрунтуйте проведені операції

# Перетворення категоріальних даних в числові
label_encoder = LabelEncoder()
new_boba['Title_encoded'] = label_encoder.fit_transform(new_boba['title'])
new_boba['RatingLevel_encoded'] = label_encoder.fit_transform(new_boba['rating'])
new_boba['RatingDescription_encoded'] = label_encoder.fit_transform(new_boba['ratingLevel'])

# Відбір значущих ознак
selected_features = ['release year', 'user rating score', 'user rating size']

# Конструювання нових ознак
new_boba['AgeAtRating'] = 2023 - new_boba['release year']
new_boba['RatingPerUser'] = new_boba['user rating score'] / new_boba['user rating size']

# Вибірка підмножини даних зі значущими ознаками
boba_subset = new_boba[selected_features + ['AgeAtRating', 'RatingPerUser']]

# Відбір числових ознак
numeric_features = ['release year', 'user rating score', 'user rating size']

# Заповнення пропущених значень
imputer = SimpleImputer(strategy='mean')  # Можна вибрати різні стратегії (середнє, медіана, і т.д.)
boba_subset[numeric_features] = imputer.fit_transform(boba_subset[numeric_features])

# Використання бінаризації для перетворення числових ознак в категоріальні
for feature in numeric_features:
    boba_subset[feature + '_binary'] = boba_subset[feature].values.reshape(-1, 1)

print(boba_subset)
boba_subset.to_csv('boba_subset.csv', index=False)
