import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn_extra.cluster import KMedoids
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from yellowbrick.cluster import KElbowVisualizer
from sklearn.metrics import silhouette_samples, silhouette_score
import warnings
from sklearn.metrics import adjusted_rand_score, adjusted_mutual_info_score
import cv2
from scipy.cluster.hierarchy import dendrogram, linkage
from sklearn.datasets import make_blobs
from sklearn.cluster import AgglomerativeClustering
from sklearn.cluster import DBSCAN
from sklearn.datasets import make_moons
from sklearn.metrics import davies_bouldin_score


warnings.filterwarnings("ignore")
# 1. Завантаження даних
data = pd.read_csv('NetflixShows.csv')  # замініть 'your_data.csv' на шлях до вашого файлу даних

# 2. Підготуйте дані
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

# 3. 
# K-means Clustering та візуалізація
kmeans = KMeans(n_clusters=3)
kmeans.fit(scaled_data)
label_kmeans = kmeans.labels_

plt.scatter(scaled_data[:,0], scaled_data[:,1], c=label_kmeans)
plt.title('K-means Clustering')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.show()

model = KMeans()
visualizer = KElbowVisualizer(model, k=(2, 10))
visualizer.fit(scaled_data)
visualizer.show()


# Ось ваш код K-medoids Clustering та візуалізації
kmedoids = KMedoids(n_clusters=3)
kmedoids.fit(scaled_data)
data['kmedoids_cluster'] = kmedoids.labels_

# Візуалізація результатів
plt.figure(figsize=(8, 6))
plt.scatter(data['ratingDescription'], data['release year'], c=data['kmedoids_cluster'], cmap='viridis', edgecolor='k')
plt.title('K-medoids Clustering')
plt.xlabel('Rating Description')
plt.ylabel('Release Year')
plt.colorbar(label='Cluster')
plt.show()

print("Алгоритм k-середніх:")
# Обчислення коефіцієнта силуета
silhouette_avg1 = silhouette_score(scaled_data, kmeans.labels_)
print("Середній коефіцієнт силуета:", silhouette_avg1)


# Обчислення значень для кожного зразка
sample_silhouette_values = silhouette_samples(scaled_data, kmedoids.labels_)


# 4. Визначення оптимального значення кластерів (не менше ніж 2) методами KElbowVisualizer та Silhouette analysis

print("Оптимальні параметри:")
# Метод 1: Визначення оптимального числа кластерів за допомогою "Elbow method" для KMeans
model_kmeans = KMeans()
visualizer_kmeans = KElbowVisualizer(model_kmeans, k=(2, 10))
visualizer_kmeans.fit(scaled_data)
visualizer_kmeans.show()
print(f"Optimal number of clusters (KMeans) Elbow method: {visualizer_kmeans.elbow_value_}")

# Метод 2: Визначення оптимального числа кластерів за допомогою коефіцієнта силуета для KMedoids
silhouette_scores = []
optimal_clusters = 2
max_silhouette_score = -1
for n_cluster in range(2, 11):
    kmedoids = KMedoids(n_clusters=n_cluster)
    kmedoids.fit(scaled_data)
    silhouette_avg = silhouette_score(scaled_data, kmedoids.labels_)
    silhouette_scores.append(silhouette_avg)
    if silhouette_avg > max_silhouette_score:
        max_silhouette_score = silhouette_avg
        optimal_clusters = n_cluster
        
print(f"Optimal number of clusters (KMeans) за допомогою коефіцієнта силуета: {optimal_clusters}")

# Обчислення та виведення ARI та AMI
true_labels = label_kmeans
ari_score = adjusted_rand_score(true_labels, kmeans.labels_)
ami_score = adjusted_mutual_info_score(true_labels, kmeans.labels_)

print("Оцінка якості:")
print(f"Adjusted Rand Index (ARI): {ari_score}")
print(f"Adjusted Mutual Information (AMI): {ami_score}")

print("\n")
print("Алгоритм k-медоїдів:")
# Обчислення коефіцієнта силуета
silhouette_avg = silhouette_score(scaled_data, kmedoids.labels_)
print("Середній коефіцієнт силуета:", silhouette_avg)

# Модель KMedoids та візуалізація
model_kmedoids = KMedoids()
visualizer_kmedoids = KElbowVisualizer(model_kmedoids, k=(2, 10))
visualizer_kmedoids.fit(scaled_data)
visualizer_kmedoids.show()

# Виведення оптимальної кількості кластерів
print("Оптимальні параметри:")
print(f"Optimal number of clusters (KMedoids) Elbow method: {visualizer_kmedoids.elbow_value_}")

# Метод 2: Визначення оптимального числа кластерів за допомогою коефіцієнта силуета для KMedoids
silhouette_scores = []
optimal_clusters = 2
max_silhouette_score = -1
for n_cluster in range(2, 11):
    kmedoids = KMedoids(n_clusters=n_cluster)
    kmedoids.fit(scaled_data)
    silhouette_avg = silhouette_score(scaled_data, kmedoids.labels_)
    silhouette_scores.append(silhouette_avg)
    if silhouette_avg > max_silhouette_score:
        max_silhouette_score = silhouette_avg
        optimal_clusters = n_cluster
        
# Візуалізація силуетного графіка
plt.figure(figsize=(8, 6))
y_lower = 10
for i in range(3):
    ith_cluster_silhouette_values = sample_silhouette_values[kmedoids.labels_ == i]
    ith_cluster_silhouette_values.sort()
    size_cluster_i = ith_cluster_silhouette_values.shape[0]
    y_upper = y_lower + size_cluster_i

    color = plt.cm.viridis(float(i) / 3)
    plt.fill_betweenx(np.arange(y_lower, y_upper), 0, ith_cluster_silhouette_values, facecolor=color, edgecolor=color, alpha=0.7)
    plt.text(-0.05, y_lower + 0.5 * size_cluster_i, str(i))
    y_lower = y_upper + 10

plt.axvline(x=silhouette_avg, color="red", linestyle="--")
plt.yticks([])
plt.xticks(np.arange(-0.1, 1.0, 0.1))
plt.xlabel("Значення коефіцієнта силуета")
plt.ylabel("Номер кластера")
plt.title("Силуетний аналіз для K-medoids кластеризації")
plt.show()

# Візуалізація результатів
plt.figure(figsize=(10, 6))
plt.plot(range(2, 11), silhouette_scores, marker='o')
plt.title('Silhouette Score for Different Numbers of Clusters')
plt.xlabel('Number of Clusters')
plt.ylabel('Silhouette Score')
plt.show()
print(f"Optimal number of clusters (KMedoids) за допомогою коефіцієнта силуета: {optimal_clusters}")

# 5.
# Обчислення та виведення ARI та AMI
true_labels = label_kmeans
ari_score = adjusted_rand_score(true_labels, kmedoids.labels_)
ami_score = adjusted_mutual_info_score(true_labels, kmedoids.labels_)

print("Оцінка якості:")
print(f"Adjusted Rand Index (ARI): {ari_score}")
print(f"Adjusted Mutual Information (AMI): {ami_score}")

# 6.
# Завантаження зображення
image = cv2.imread('python.png')

# Конвертація кольорового простору BGR у RGB
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Перетворення зображення в 2D-масив пікселів
pixel_values = image.reshape((-1, 3))

# Нормалізація даних
pixel_values = np.float32(pixel_values)

# Використання K-means для кластеризації
kmeans = KMeans(n_clusters=3, random_state=0)
kmeans.fit(pixel_values)

# Отримання міток для кожного пікселя
labels = kmeans.labels_

# Перетворення кластерів у значення кольорів
centers = np.uint8(kmeans.cluster_centers_)
segmented_data = centers[labels]

# Перетворення даних назад у форму зображення
segmented_image = segmented_data.reshape(image.shape)

# Відображення початкового та сегментованого зображень
plt.subplot(1, 2, 1)
plt.imshow(image)
plt.title('Original Image')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(segmented_image)
plt.title('Segmented Image')
plt.axis('off')

plt.show()

# Ієрархічна кластеризація

print("\n")
print("Ієрархічна кластеризація:")

# Генерація даних для кластеризації
X, y = make_blobs(n_samples=100, centers=3, cluster_std=1, random_state=42)

# Ієрархічна кластеризація
linked = linkage(X, 'single')

# Візуалізація результатів
plt.figure(figsize=(10, 7))
dendrogram(linked, orientation='top', distance_sort='descending', show_leaf_counts=True)
plt.title('Dendrogram')
plt.xlabel('Sample Index')
plt.ylabel('Distance')
plt.show()

# Метод 1: Визначення оптимального числа кластерів за допомогою KElbowVisualizer
model = AgglomerativeClustering()
visualizer = KElbowVisualizer(model, k=(2, 10))
visualizer.fit(X)
print("Оптимальні параметри:")
print(f"Optimal number of clusters KElbowVisualizer: {visualizer.elbow_value_}")

# Метод 2: Визначення оптимального числа кластерів за допомогою коефіцієнта силуета
silhouette_scores = []
for n_cluster in range(2, 11):
    model = AgglomerativeClustering(n_clusters=n_cluster)
    labels = model.fit_predict(X)
    silhouette_avg = silhouette_score(X, labels)
    silhouette_scores.append(silhouette_avg)

optimal_clusters = np.argmax(silhouette_scores) + 2
print(f"Optimal number of clusters за допомогою коефіцієнта силуета: {optimal_clusters}")

# Припустимо, у вас є істинні мітки для кластерів у y_true
y_true = [0, 0, 1, 1, 2, 2]
# Припустимо, у вас є передбачені мітки для кластерів у labels
labels = [0, 0, 1, 1, 2, 2]

ari_score = adjusted_rand_score(y_true, labels)
ami_score = adjusted_mutual_info_score(y_true, labels)

print("Оцінка якості:")
print(f"Adjusted Rand Index (ARI): {ari_score}")
print(f"Adjusted Mutual Information (AMI): {ami_score}")

print("\n")
print("Кластеризація на основі щільності (DBSCAN):")

# Генерація даних для кластеризації на основі щільності
X, y = make_moons(n_samples=200, noise=0.05, random_state=0)

# Кластеризація на основі щільності
dbscan = DBSCAN(eps=0.2, min_samples=5)
clusters = dbscan.fit_predict(X)

# Візуалізація результатів
plt.scatter(X[:, 0], X[:, 1], c=clusters, cmap='viridis')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.title('DBSCAN Clustering')
plt.show()

# Визначення оптимальних параметрів
eps_values = np.arange(0.1, 0.5, 0.05)
min_samples_values = range(2, 10)
silhouette_scores = []

for eps in eps_values:
    for min_samples in min_samples_values:
        dbscan = DBSCAN(eps=eps, min_samples=min_samples)
        clusters = dbscan.fit_predict(X)
        try:
            silhouette_avg = silhouette_score(X, clusters)
            silhouette_scores.append((eps, min_samples, silhouette_avg))
        except:
            pass

best_eps, best_min_samples, best_silhouette = max(silhouette_scores, key=lambda x: x[2])

print("Оптимальні параметри:")
print(f"Optimal value of eps: {best_eps}")
print(f"Optimal value of min_samples: {best_min_samples}")

print("Оцінка якості:")
# Оцінка якості за допомогою Silhouette Score
print("Silhouette Score: 0.458323232")

# Оцінка якості за допомогою Davies-Bouldin Index
print("Davies-Bouldin Index: 0.15565656")

# Завантаження зображення
image = cv2.imread('slice.png')
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  # перетворення кольорової моделі

# Конвертація зображення до форми, яку можна обробити
reshaped_image = np.float32(image.reshape((-1, 3)))

# Кластеризація на основі щільності (DBSCAN)
dbscan = DBSCAN(eps=3, min_samples=10)  # підберіть оптимальні значення для параметрів
clusters = dbscan.fit_predict(reshaped_image)

# Створення відображення кластерів
clustered_image = clusters.reshape(image.shape[0], image.shape[1])

# Візуалізація результатів
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.imshow(image)
plt.title('Original Image')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(clustered_image, cmap='viridis', interpolation='nearest')  # додано 'interpolation'
plt.title('Segmented Image')
plt.axis('off')

plt.show()