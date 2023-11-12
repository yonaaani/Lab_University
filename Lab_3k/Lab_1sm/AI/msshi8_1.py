import numpy as np

# Функція мінімаксної нормалізації
def min_max_normalization(data):
    normalized_data = (data - np.min(data)) / (np.max(data) - np.min(data))
    return normalized_data

# Вхідні дані (числа для множення)
numbers = []

# Кількість чисел, які користувач хоче перемножити
num_count = int(input("Введіть кількість чисел для множення: "))
for i in range(num_count):
    number = float(input(f"Введіть число {i + 1}: "))
    numbers.append(number)

input_size = len(numbers)

# Створення перцептрона для множення
class MultiplicationPerceptron:
    def __init__(self, input_size, hidden_size, output_size, activation_function='linear'):
        self.weights_input_hidden = np.random.randn(hidden_size, input_size) * 0.1  # Better weight initialization
        self.weights_hidden_output = np.random.randn(output_size, hidden_size) * 0.1
        self.activation_function = activation_function

    def forward(self, inputs):
        hidden = np.dot(self.weights_input_hidden, inputs)
        
        if self.activation_function == 'linear':
            activation = hidden
        elif self.activation_function == 'sigmoid':
            activation = 1 / (1 + np.exp(-hidden))
        else:
            raise ValueError("Invalid activation function. Choose 'linear' or 'sigmoid'.")
        
        output = np.dot(self.weights_hidden_output, activation)
        return output

# Параметри мережі для множення
hidden_size = int(input("Введіть кількість персептронів на прихованому шарі: "))
output_size = 1  # Одне число вихід

# Вибір функції активації
activation_choice = input("Виберіть функцію активації ('linear' або 'sigmoid'): ")

# Створення об'єкту перцептрона для множення
multiplication_perceptron = MultiplicationPerceptron(input_size, hidden_size, output_size, activation_choice)

# Навчання перцептрона для множення
learning_rate = 0.01  # Adjusted learning rate
epochs = 1000  # Increased epochs for better convergence

# Приклади вхідних та вихідних даних для навчання (множення)
input_data = np.array(numbers)
output_data = np.array([np.prod(numbers)])  # Вихідні дані (результат множення)

# Навчання перцептрона з використанням алгоритму зворотного поширення помилки
for epoch in range(epochs):
    normalized_data = min_max_normalization(input_data)
    target = output_data
    output = multiplication_perceptron.forward(normalized_data)

    # Обчислення похибки
    error = target - output

    # Зворотне поширення помилки
    output_delta = error
    
    if activation_choice == 'linear':
        hidden = np.maximum(np.dot(multiplication_perceptron.weights_input_hidden, normalized_data), 0)
    elif activation_choice == 'sigmoid':
        hidden = 1 / (1 + np.exp(-np.dot(multiplication_perceptron.weights_input_hidden, normalized_data)))
    else:
        raise ValueError("Invalid activation function. Choose 'linear' or 'sigmoid'.")
    
    hidden_delta = np.dot(multiplication_perceptron.weights_hidden_output.T, output_delta) * hidden

    multiplication_perceptron.weights_hidden_output += learning_rate * np.outer(output_delta, hidden)
    multiplication_perceptron.weights_input_hidden += learning_rate * np.outer(hidden_delta, normalized_data)

# Вивід результату множення
result = multiplication_perceptron.forward(min_max_normalization(np.array(numbers)))
print("Результат множення:", result[0])
