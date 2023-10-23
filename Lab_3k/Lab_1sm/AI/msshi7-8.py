import numpy as np

# Функція активації - сигмоїда
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# Похідна сигмоїди
def sigmoid_derivative(x):
    return x * (1 - x)

# Введення кількості симптомів
num_symptoms = 4

# Запитуємо користувача про наявність кожного симптома
symptoms = []
print("Вкажіть наявність кожного з наступних симптомів (1 - так, 0 - ні):")
symptoms.append(int(input("Чи є висока температура? ")))
symptoms.append(int(input("Чи є біль у горлі? ")))
symptoms.append(int(input("Чи є кашель? ")))
symptoms.append(int(input("Чи є слабкість? ")))

# Перетворення списку симптомів у масив NumPy
X = np.array(symptoms).reshape(1, -1)

# Введення вихідних даних для грипу
# 1 - якщо пацієнт хворий на грип, 0 - якщо пацієнт не хворий на грип
Y = np.array([[int(input("Чи хворий пацієнт на грип? (1 - так, 0 - ні): "))]])

# Встановлення випадкових ваг для початку
np.random.seed(0)
input_layer_size = num_symptoms
hidden_layer_size = 4
output_layer_size = 1

# Ініціалізація ваг і зсувів з випадковими значеннямиі
weights_input_hidden = np.random.uniform(size=(input_layer_size, hidden_layer_size))
bias_hidden = np.random.uniform(size=(1, hidden_layer_size))
weights_hidden_output = np.random.uniform(size=(hidden_layer_size, output_layer_size))
bias_output = np.random.uniform(size=(1, output_layer_size))

# Навчання мережі
learning_rate = 0.1
epochs = 10000
max_error = 0  # Ініціалізація максимальної похибки

for epoch in range(epochs):
    # Прямий прохід (forward pass)
    hidden_layer_input = np.dot(X, weights_input_hidden) + bias_hidden
    hidden_layer_output = sigmoid(hidden_layer_input)
    output_layer_input = np.dot(hidden_layer_output, weights_hidden_output) + bias_output
    output_layer_output = sigmoid(output_layer_input)

    # Обчислення помилки
    error = Y - output_layer_output
    
    # Обчислення максимальної похибки
    current_max_error = np.max(np.abs(error))  # Знаходження максимальної похибки
    if current_max_error > max_error:  # Порівняння з максимальною знайденою похибкою
        max_error = current_max_error  # Оновлення максимальної похибки, якщо необхідно

    # Зворотній прохід (backpropagation)
    d_output = error * sigmoid_derivative(output_layer_output)
    error_hidden_layer = d_output.dot(weights_hidden_output.T)
    d_hidden_layer = error_hidden_layer * sigmoid_derivative(hidden_layer_output)

    # Оновлення ваг і зсувів
    weights_hidden_output += hidden_layer_output.T.dot(d_output) * learning_rate
    bias_output += np.sum(d_output, axis=0, keepdims=True) * learning_rate
    weights_input_hidden += X.T.dot(d_hidden_layer) * learning_rate
    bias_hidden += np.sum(d_hidden_layer, axis=0, keepdims=True) * learning_rate
    
    # Перевірка максимальної різниці між бажаним і прогнозованим виходами персептрона
    if max_error < 0.1:  # Перевірка, чи максимальна похибка менше заданого порогу
        break  # Зупинка навчання, якщо умова виконана
        
# Виведення максимальної похибки після завершення всіх епох
print(f"Максимальна похибка: {max_error}")

# Виведення результатів
print("Результати після навчання:")
print(output_layer_output)
