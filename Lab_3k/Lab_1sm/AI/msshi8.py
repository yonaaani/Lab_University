import numpy as np

class MultiplicationPerceptron:
    def __init__(self, input_size, hidden_size, output_size):
        # Використовуємо He ініціалізацію для ваг
        self.weights_input_hidden = np.random.randn(hidden_size, input_size) * np.sqrt(2 / input_size)
        self.weights_hidden_output = np.random.randn(output_size, hidden_size) * np.sqrt(2 / hidden_size)

    def relu(self, x):
        return np.maximum(x, 0)

    def forward(self, inputs):
        hidden = np.dot(self.weights_input_hidden, inputs)
        hidden = self.relu(hidden)
        output = np.dot(self.weights_hidden_output, hidden).reshape(-1, 1)
        return output

# Параметри мережі
hidden_size = 8
output_size = 1

# Створення об'єкту перцептрона
multiplication_perceptron = MultiplicationPerceptron(2, hidden_size, output_size)

# Навчання перцептрона з нормалізацією входів
learning_rate = 0.01
epochs = 1000

# Вхідні та вихідні дані для навчання
input_data = np.array([[i, j] for i in range(1, 11) for j in range(1, 11)])
output_data = np.array([i * j for i in range(1, 11) for j in range(1, 11)])

# Нормалізація вхідних даних
normalized_input_data = input_data / 10.0  # Припускаємо, що значення вхідних даних знаходяться від 1 до 10

# Навчання перцептрона
for epoch in range(epochs):
    for i in range(len(normalized_input_data)):
        target = np.array([output_data[i]])
        output = multiplication_perceptron.forward(normalized_input_data[i].reshape(-1, 1))

        # Обчислення помилки
        error = target - output

        # Зворотнє поширення помилки
        output_delta = error

        # Derivative of the ReLU activation function
        hidden = np.dot(multiplication_perceptron.weights_input_hidden, normalized_input_data[i].reshape(-1, 1))
        hidden_derivative = (hidden > 0).astype(float)
        hidden_delta = np.dot(multiplication_perceptron.weights_hidden_output.T, output_delta) * hidden_derivative

        # Оновлення ваг
        multiplication_perceptron.weights_hidden_output += learning_rate * np.outer(output_delta, hidden)
        multiplication_perceptron.weights_input_hidden += learning_rate * np.outer(hidden_delta, normalized_input_data[i].reshape(-1, 1))

# Check the model prediction on training data again
for i in range(len(normalized_input_data)):
    result = multiplication_perceptron.forward(normalized_input_data[i].reshape(-1, 1))
    print(f"Input: {input_data[i]}, Target: {output_data[i]}, Predicted: {result[0, 0]:.2f}")
    
# Введення користувача та виведення результату з нормалізацією входів
while True:
    try:
        user_input = input("Введіть два числа через пробіл (або 'exit' для виходу): ")
        if user_input.lower() == 'exit':
            break
        nums = [int(num) for num in user_input.split()]
        normalized_user_input = np.array(nums) / 10.0  # Нормалізація введених користувачем даних
        result = multiplication_perceptron.forward(normalized_user_input.reshape(-1, 1))
        print(f"Результат множення: {result[0, 0]:.2f}")
    except ValueError:
        print("Будь ласка, введіть два числа.")
