import pandas as pd
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules
from mlxtend.frequent_patterns import fpgrowth
import warnings
from sklearn.preprocessing import LabelEncoder
import time
from memory_profiler import profile
import seaborn as sns
import matplotlib.pyplot as plt

warnings.filterwarnings("ignore")

# 1. Завантаження даних
data = pd.read_csv('NetflixShows.csv')

# 2. Підготовка даних
data['title'] = data['title'].astype('str')
data['rating'] = data['rating'].astype('str')
data['ratingLevel'] = data['ratingLevel'].astype('str')

# Заповнення відсутніх значень
data['ratingDescription'].fillna(data['ratingDescription'].mean(), inplace=True)
data['release year'].fillna(data['release year'].mean(), inplace=True)
data['user rating score'].fillna(data['user rating score'].mean(), inplace=True)
data['user rating size'].fillna(data['user rating size'].mean(), inplace=True)

# Кодування категоріальних ознак
labelencoder = LabelEncoder()
data['title'] = labelencoder.fit_transform(data['title'])
data['rating'] = labelencoder.fit_transform(data['rating'])
data['ratingLevel'] = labelencoder.fit_transform(data['ratingLevel'])

data_transformed = pd.get_dummies(data)
data_transformed = data_transformed.astype(bool)

print(data_transformed.head())
print("")
print(data_transformed.dtypes)

# 3. На основі підготовлених даних з застосуванням алгоритму apriori сформувати набір асоціативних правил.
frequent_itemsets = apriori(data_transformed, min_support=0.2, use_colnames=True)
rules = association_rules(frequent_itemsets, metric="lift", min_threshold=1)

top_rules = rules.nlargest(5, 'support')
print("Застосування алгоритму apriori:")
print(top_rules)

# 4. На основні власних даних з застосуванням алгоритму FP-growth сформувати набір асоціативних правил.
# Застосування алгоритму FP-growth
frequent_itemsets_fp = fpgrowth(data_transformed, min_support=0.2, use_colnames=True)
rules_fp = association_rules(frequent_itemsets_fp, metric="lift", min_threshold=1)
print("Застосування алгоритму FP-growth:")

# Виведення результатів
print(rules_fp)

# 5. Застосування алгоритму ECLAT
print("Застосування алгоритму ECLAT:")
# Використання алгоритму Eclat для знаходження часто встречаються наборів
frequent_itemsets_eclat = apriori(data_transformed, min_support=0.2, use_colnames=True)

# Створення асоціативних правил
rules_eclat = association_rules(frequent_itemsets_eclat, metric="confidence", min_threshold=0.7)
print(rules_eclat)

# 6. Оцінка показників якості

@profile
def run_apriori():
    start_time_apriori = time.time()
    frequent_itemsets_apriori = apriori(data_transformed, min_support=0.2, use_colnames=True)
    end_time_apriori = time.time()
    execution_time_apriori = end_time_apriori - start_time_apriori
    print("Оцінка для алгоритму apriori:")
    print(frequent_itemsets_apriori)
    print("Час виконання для алгоритму apriori: ", execution_time_apriori, " секунд")

@profile
def run_fpgrowth():
    start_time_fp = time.time()
    frequent_itemsets_fp = fpgrowth(data_transformed, min_support=0.2, use_colnames=True)
    end_time_fp = time.time()
    execution_time_fp = end_time_fp - start_time_fp
    print("Оцінка для алгоритму FP-growth:")
    print(frequent_itemsets_fp)
    print("Час виконання для алгоритму FP-growth: ", execution_time_fp, " секунд")

@profile
def run_eclat():
    start_time_eclat = time.time()
    frequent_itemsets_eclat = apriori(data_transformed, min_support=0.2, use_colnames=True)
    end_time_eclat = time.time()
    execution_time_eclat = end_time_eclat - start_time_eclat
    print("Оцінка для алгоритму ECLAT:")
    print(frequent_itemsets_eclat)
    print("Час виконання для алгоритму ECLAT: ", execution_time_eclat, " секунд")

run_apriori()
run_fpgrowth()
run_eclat()

# 7.  На  основі п.6 здійснити пошук та видалення надлишкових правил.

def prune_rules(rules, min_confidence=0.5):
    pruned_rules = rules[rules['confidence'] >= min_confidence]
    return pruned_rules

# Виклик функції для кожного алгоритму
min_confidence = 0.6
pruned_rules_apriori = prune_rules(rules, min_confidence)
pruned_rules_fp = prune_rules(rules_fp, min_confidence)
pruned_rules_eclat = prune_rules(rules_eclat, min_confidence)

# Виведення результатів
print("Надлишкові правила після очищення за пороговим значенням confidence:", min_confidence)
print("Для алгоритму apriori:")
print(pruned_rules_apriori)
print("Для алгоритму FP-growth:")
print(pruned_rules_fp)
print("Для алгоритму ECLAT:")
print(pruned_rules_eclat)

# 8. Візуалізувати отримані в п.7. набори правил та провести їх інтерпретацію.

# Візуалізація для алгоритму apriori
sns.scatterplot(data=pruned_rules_apriori, x='support', y='confidence', hue='lift')
plt.title('Асоціативні правила для apriori')
plt.show()

# Візуалізація для алгоритму FP-growth
sns.scatterplot(data=pruned_rules_fp, x='support', y='confidence', hue='lift')
plt.title('Асоціативні правила для FP-growth')
plt.show()

# Візуалізація для алгоритму ECLAT
sns.scatterplot(data=pruned_rules_eclat, x='support', y='confidence', hue='lift')
plt.title('Асоціативні правила для ECLAT')
plt.show()