import numpy as np

# Функція мінімаксної нормалізації
def min_max_normalization(data):
    normalized_data = (data - np.min(data)) / (np.max(data) - np.min(data))
    return normalized_data

# Вхідні дані (симптоми)
symptoms = ['Насморк', 'Тошнота', 'Кашель', 'Сухість горла', 'Головні болі', 'Хрипи', 'Чхання', 'Болі в грудях', 'Temneparypa', 'Відсутність апетиту', 'Порушення сну', 'Болі в м’язах']
input_size = len(symptoms)

# Створення перцептрона
class Perceptron:
    def __init__(self, input_size, hidden_size, output_size):
        self.weights_input_hidden = np.random.rand(hidden_size, input_size)
        self.weights_hidden_output = np.random.rand(output_size, hidden_size)

    def forward(self, inputs):
        hidden = np.dot(self.weights_input_hidden, inputs)
        hidden = np.maximum(hidden, 0)  
        output = np.dot(self.weights_hidden_output, hidden)
        return output

# Параметри мережі
hidden_size = 3  # Рекомендоване значення, але може бути змінене
output_size = 3  # Кількість можливих діагнозів

# Створення об'єкту перцептрона
perceptron = Perceptron(input_size, hidden_size, output_size)

# Навчання перцептрона
learning_rate = 0.1
epochs = 50

# Приклади вхідних та вихідних даних для навчання
input_data_1 = np.array([3, 1, 3, 2, 1, 3, 2, 0, 2, 2, 0, 0])  # Вхідні дані (симптоми)
output_data_1 = np.array([1, 0, 0])  # Вихідні дані (Грип)

input_data_2 = np.array([0, 3, 0, 1, 1, 0, 0, 1, 2, 3, 1, 0])  # Вхідні дані (симптоми)
output_data_2 = np.array([0, 1, 0])  # Вихідні дані (Гастрит)

input_data_3 = np.array([1, 0, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0])  # Вхідні дані (симптоми)
output_data_3 = np.array([0, 0, 1])  # Вихідні дані (Здоров-ий/а)

# Функція для постановки діагнозу
def make_diagnosis(user_input):
    normalized_user_input = min_max_normalization(user_input)
    output = perceptron.forward(normalized_user_input)
    output_percentage = 100 * (np.exp(output) / np.sum(np.exp(output)))
    possible_diagnoses = ['Грип', 'Гастрит', 'Здоров-ий/а']
    for i in range(len(possible_diagnoses)):
        print(f"{possible_diagnoses[i]}: {output_percentage[i]:.2f}%")
    diagnosis_index = np.argmax(output_percentage)
    return possible_diagnoses[diagnosis_index]


# Запитання користувачу та отримання відповідей
user_input = []
for symptom in symptoms:
    answer = int(input(f"Як сильно ви проявляєте симптом {symptom}? (Від 0 до 3): "))
    user_input.append(answer)

# Навчання перцептрона з використанням алгоритму зворотного поширення помилки
for epoch in range(epochs):
    for i, data in enumerate([input_data_1, input_data_2, input_data_3]):
        normalized_data = min_max_normalization(data)
        target = np.array([output_data_1, output_data_2, output_data_3][i])
        output = perceptron.forward(normalized_data)

        # Обчислення похибки
        error = target - output

        # Зворотне поширення помилки
        output_delta = error
        hidden = np.dot(perceptron.weights_input_hidden, normalized_data)
        hidden[hidden <= 0] = 0
        hidden[hidden > 0] = 1
        hidden_delta = np.dot(perceptron.weights_hidden_output.T, output_delta) * hidden

        perceptron.weights_hidden_output += learning_rate * np.outer(output_delta, hidden)
        perceptron.weights_input_hidden += learning_rate * np.outer(hidden_delta, normalized_data)

# Вивід діагнозу
diagnosis = make_diagnosis(user_input)
print("Діагноз:", diagnosis)