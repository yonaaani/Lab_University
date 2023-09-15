import random

#1. Ініціалізація синаптичних ваг та порогу чутливості
num_inputs = 12
weights = [random.uniform(-0.1, 0.1) for _ in range(num_inputs)]
threshold = random.uniform(-0.1, 0.1)
learning_rate = 0.1  # Швидкість навчання

#2. Функція для визначення вихідного сигналу персептрона
def compute_output(inputs):
    weighted_sum = sum(w * x for w, x in zip(weights, inputs))
    return 1 if weighted_sum >= threshold else 0

# Оголошення матриць для кожної цифри
digits = [
    [[1, 1, 1], [1, 0, 1], [1, 0, 1], [1, 1, 1]],  # 0
    [[0, 0, 1], [0, 0, 1], [0, 0, 1], [0, 0, 1]],  # 1
    [[1, 1, 1], [0, 0, 1], [1, 1, 1], [1, 0, 0]],  # 2
    [[1, 1, 1], [0, 0, 1], [1, 1, 1], [0, 0, 1]],  # 3
    [[1, 0, 1], [1, 0, 1], [1, 1, 1], [0, 0, 1]],  # 4
    [[1, 1, 1], [1, 0, 0], [1, 1, 1], [0, 0, 1]],  # 5
    [[1, 1, 1], [1, 0, 0], [1, 1, 1], [1, 0, 1]],  # 6
    [[1, 1, 1], [0, 0, 1], [0, 0, 1], [0, 0, 1]],  # 7
    [[1, 1, 1], [1, 0, 1], [1, 1, 1], [1, 0, 1]],  # 8
    [[1, 1, 1], [1, 0, 1], [1, 1, 1], [0, 0, 1]]   # 9
]

# Навчання персептрона
def train_perceptron(num_epochs):
    for epoch in range(num_epochs):
        errors = 0
        for num in range(10):  # Перевіряємо числа від 0 до 9 по порядку
            inputs_matrix = digits[num]
            inputs = [item for sublist in inputs_matrix for item in sublist]
            
            # Визначаємо очікуваний вихід (відомо, чи цифра парна, чи ні)
            target_output = 1 if num % 2 == 0 else 0
            output = compute_output(inputs)

            #3-4. Коригуємо синаптичні ваги згідно з методом корекції
            if output != target_output:
                errors += 1
                if output == 0:
                    for i in range(num_inputs):
                        if inputs[i] == 1:
                            weights[i] += learning_rate #4.б - w+x
                else:
                    for i in range(num_inputs):
                        if inputs[i] == 1:
                            weights[i] -= learning_rate #4.в - w-x
        print(f"Епоха {epoch + 1}: {errors} помилок")


# Тренування персептрона
train_perceptron(10)

# Перевірка розпізнавання чисел
for num in range(10):
    inputs_matrix = digits[num]
    inputs = [item for sublist in inputs_matrix for item in sublist]
    output = compute_output(inputs)
    parity = "парне" if num % 2 == 0 else "непарне"
    print(f"Цифра: {num}\nВихід: {output}, Парність: {parity}")

# Виведення синаптичних ваг і порогу чутливості
print("Синаптичні ваги:")
for i, weight in enumerate(weights):
    print(f"Вага {i + 1}: {weight:.4f}")

print(f"Поріг чутливості: {threshold:.4f}")