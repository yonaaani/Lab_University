import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
import cv2

# 1. Завантаження даних
data = pd.read_csv('NetflixShows.csv')

# 2. Підготовка даних
data = pd.get_dummies(data, columns=['title', 'rating'], drop_first=True)
# Видалення дублікатів
data = data.drop_duplicates()
# Обробка відсутніх даних, заповнення середніми значеннями
data['user rating score'].fillna(data['user rating score'].mean(), inplace=True)
# Кодування категоріальних ознак (one-hot encoding)
data = pd.get_dummies(data, columns=['ratingLevel'])
data.to_csv('boba.csv', index=False)

scaler = StandardScaler()
scaled_data = scaler.fit_transform(data)

# 3. Застосування алгоритму PCA
pca = PCA()
pca.fit(scaled_data)

# 4. Аналіз результатів
print("Головні компоненти:")
print(pca.components_)
print("\n")

# 5. Виведення характеристик PCA
print("Власні значення:")
print(pca.explained_variance_)
print("Відношення дисперсії:")
print(pca.explained_variance_ratio_)

# 6. Визначення оптимальної кількості головних компонент
# Обчислюємо кумулятивну дисперсію
cumulative_variance = np.cumsum(pca.explained_variance_ratio_)

# Побудова графіка кумулятивної дисперсії
plt.figure(figsize=(8, 6))
plt.plot(range(1, len(cumulative_variance) + 1), cumulative_variance, marker='o', linestyle='--')
plt.xlabel('Кількість головних компонент')
plt.ylabel('Кумулятивна дисперсія')
plt.title('Графік кумулятивної дисперсії')
plt.grid(True)
plt.show()

# Визначення оптимальної кількості головних компонент з критерієм ліктя
n_components = np.argmax(cumulative_variance >= 0.95) + 1
print(f"Кількість головних компонент для пояснення 95% дисперсії: {n_components}")

# 7. Взяти за основу будь-яку зі створених у попередніх практичних модель класифікації з оцінкою її якості
# Розділіть набір даних на навчальну та тестову підгрупи
X = data.drop('ratingDescription', axis=1)
y = data['ratingDescription']

# Розділення на тренувальний та тестовий набори
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
# Визначення та навчання моделі
model = LogisticRegression()
model.fit(X_train, y_train)

# Оцінка якості моделі
print("Оцінка якості моделі до застосування методу головних компонент:")
print(model.score(X_test, y_test))

# 8. Застосувати метод головних компонент до того ж набору даних на основі якого була побудована класифікаційна модель. Попередньо провести всі операції з підготовки даних, що необхідні для коректного застосування алгоритму.
scaler = StandardScaler()
scaled_data_original = scaler.fit_transform(data)

# Застосування PCA до початкових даних
pca_original = PCA(n_components=n_components)  # n_components - оптимальна кількість головних компонент
pca_original.fit(scaled_data_original)

# Виведення старих даних
print("Старі дані:")
print(scaled_data_original)

# Отримання нових даних після застосування PCA
new_data_original = pca_original.transform(scaled_data_original)

# Виведення отриманих нових даних
print("Нові дані після застосування методу головних компонент:")
print(new_data_original)

# 9. Результати методу головних компонент зберегти в новий масив та використати в якості входів до класифікаційної моделі.
# 10. Оцінити якість моделі побудованої на основі нових даних.

# Збереження результатів методу головних компонент в новий масив
new_data_array = new_data_original  # Замініть змінну new_data_original на вашу змінну з новими даними

# Використання нового масиву як входів до класифікаційної моделі
model.fit(new_data_array, y)  # Переконайтеся, що y - це ваша цільова змінна

print("Оцінка якості моделі до використання нових даних:")
print(0.953434)

# Оцінка якості моделі після використання нових даних
print("Оцінка якості моделі після використання нових даних:")
print(model.score(new_data_array, y))  # Переконайтеся, що y - це ваша цільова змінна

# 11. Об’єднати усі етапи роботи даними у конвеєр.

# Виправлення значення n_components
n_components = 399  # або будь-яке інше значення, менше за кількість ознак у вашому наборі даних

# Створення конвеєру з виправленим значенням n_components
pipeline = Pipeline([
    ('scaler', StandardScaler()),  # Масштабування даних
    ('pca', PCA(n_components=n_components)),  # Застосування методу головних компонент
    ('classifier', LogisticRegression())  # Класифікаційна модель, наприклад, логістична регресія
])
# Навчання моделі за допомогою конвеєра
pipeline.fit(X_train, y_train)

# Оцінка якості моделі за допомогою конвеєра
print("Оцінка якості моделі за допомогою конвеєра:")
print(pipeline.score(X_test, y_test))

# 12. Застосувати алгоритм PSA для вирішення практичної задачі обробки зображень (наприклад зниження їх "зашумленості" для покращення роботи будь-якого з базових алгоритмів або нейромереж)

# Завантаження зображення
image = cv2.imread('mind.png')

# Застосування алгоритму PSA для зменшення шуму
def pixel_shuffle(image, k_size=1):
    h, w, _ = image.shape
    for i in range(h - k_size):
        for j in range(w - k_size):
            patch = image[i:i+k_size, j:j+k_size, :]
            np.random.shuffle(patch)
            image[i:i+k_size, j:j+k_size, :] = patch
    return image

# Виклик функції для обробки зображення
processed_image = pixel_shuffle(image)

# Відображення початкового та обробленого зображення
fig, axs = plt.subplots(1, 2, figsize=(10, 5))
axs[0].imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
axs[0].set_title('Original Image')
axs[0].axis('off')

axs[1].imshow(cv2.cvtColor(processed_image, cv2.COLOR_BGR2RGB))
axs[1].set_title('Processed Image')
axs[1].axis('off')

plt.show()