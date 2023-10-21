import numpy as np  

# Функція активації - сигмоїда
def sigmoid(x):
    return 1 / (1 + np.exp(-x))  

# Похідна сигмоїди
def sigmoid_derivative(x):
    return x * (1 - x)  

# Вхідні дані для навчання
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])  

# Вихідні дані для навчання
Y = np.array([[0], [1], [1], [0]])  

# Встановлення випадкових ваг для початку
np.random.seed(0)  
input_layer_size = 2  # Розмір вхідного шару
hidden_layer_size = 4  # Розмір прихованого шару
output_layer_size = 1  # Розмір вихідного шару

# Ініціалізація ваг і зсувів з випадковими значеннями
weights_input_hidden = np.random.uniform(size=(input_layer_size, hidden_layer_size))  # Ваги між вхідним та прихованим шарами
bias_hidden = np.random.uniform(size=(1, hidden_layer_size))  # Зсув на прихованому шарі
weights_hidden_output = np.random.uniform(size=(hidden_layer_size, output_layer_size))  # Ваги між прихованим та вихідним шарами
bias_output = np.random.uniform(size=(1, output_layer_size))  # Зсув на вихідному шарі

# Навчання мережі
learning_rate = 0.1  # Швидкість навчання
epochs = 10000  # Кількість епох навчання
max_error = 0  # Ініціалізація максимальної похибки

for epoch in range(epochs):  # Цикл для кожної епохи

    # Прямий прохід (forward pass)
    hidden_layer_input = np.dot(X, weights_input_hidden) + bias_hidden  # Обчислення вхідного сигналу на прихованому шарі
    hidden_layer_output = sigmoid(hidden_layer_input)  # Вихідний сигнал на прихованому шарі після застосування функції активації
    output_layer_input = np.dot(hidden_layer_output, weights_hidden_output) + bias_output  # Обчислення вхідного сигналу на вихідному шарі
    output_layer_output = sigmoid(output_layer_input)  # Вихідний сигнал на вихідному шарі після застосування функції активації

    # Обчислення помилки
    error = Y - output_layer_output  # Обчислення різниці між фактичними та прогнозованими значеннями

    # Обчислення максимальної похибки
    current_max_error = np.max(np.abs(error))  # Знаходження максимальної похибки
    if current_max_error > max_error:  # Порівняння з максимальною знайденою похибкою
        max_error = current_max_error  # Оновлення максимальної похибки, якщо необхідно

    # Зворотній прохід (backpropagation)
    d_output = error * sigmoid_derivative(output_layer_output)  # Обчислення помилки на вихідному шарі
    error_hidden_layer = d_output.dot(weights_hidden_output.T)  # Обчислення помилки на прихованому шарі
    d_hidden_layer = error_hidden_layer * sigmoid_derivative(hidden_layer_output)  # Обчислення помилки на прихованому шарі

    # Оновлення ваг і зсувів
    weights_hidden_output += hidden_layer_output.T.dot(d_output) * learning_rate  # Оновлення ваг між прихованим та вихідним шарами
    bias_output += np.sum(d_output, axis=0, keepdims=True) * learning_rate  # Оновлення зсуву на вихідному шарі
    weights_input_hidden += X.T.dot(d_hidden_layer) * learning_rate  # Оновлення ваг між вхідним та прихованим шарами
    bias_hidden += np.sum(d_hidden_layer, axis=0, keepdims=True) * learning_rate  # Оновлення зсуву на прихованому шарі

    # Перевірка максимальної різниці між бажаним і прогнозованим виходами персептрона
    if max_error < 0.1:  # Перевірка, чи максимальна похибка менше заданого порогу
        break  # Зупинка навчання, якщо умова виконана
    

# Виведення максимальної похибки після завершення всіх епох
print(f"Максимальна похибка: {max_error}")

# Виведення результатів
print("Результати після навчання:")
print(output_layer_output)
