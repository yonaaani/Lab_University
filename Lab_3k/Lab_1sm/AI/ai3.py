import tkinter as tk
from PIL import Image, ImageDraw
import numpy as np

# Функція активації (порогова функція)
def activation_function(x):
    return 1 if x >= 0 else 0

# Функція для розпізнавання букви
def recognize_letter():
    # Отримання вхідних даних з малюнка
    input_data = get_input_data()
    
    # Зважене підсумовування вхідних сигналів
    weighted_sum = np.dot(input_data, weights) + bias
    
    # Вихід нейрона після застосування функції активації
    output = activation_function(weighted_sum)
    
    if output == 1:
        result_label.config(text="Буква А визнана")
    else:
        result_label.config(text="Буква А не визнана")
    
    # Очищення canvas
    clear_canvas()

# Функція для отримання вхідних даних з малюнка
def get_input_data():
    # Отримання малюнка з canvas і перетворення його в numpy масив
    img = Image.new("L", (28, 28), 0)  # Створення чорного зображення 28x28 пікселів
    draw = ImageDraw.Draw(img)
    
    for point in drawn_points:
        draw.ellipse([point[0] - 3, point[1] - 3, point[0] + 3, point[1] + 3], fill=255)
    
    img_array = np.array(img).flatten()  # Перетворення зображення в одномірний масив
    
    return img_array

# Функція для очищення canvas
def clear_canvas():
    canvas.delete("all")
    global drawn_points
    drawn_points = []

# Ініціалізація вагових коефіцієнтів та нейронного зміщення (як у попередньому коді)
input_neurons = 28 * 28  # 28x28 пікселів для зображення
output_neurons = 1
weights = np.random.rand(input_neurons)
bias = np.random.rand()

# Створення GUI за допомогою Tkinter
window = tk.Tk()
window.title("Розпізнавання букви")
window.geometry("400x400")

canvas = tk.Canvas(window, width=300, height=300, bg="white")
canvas.pack()

recognize_button = tk.Button(window, text="Розпізнати букву", command=recognize_letter)
recognize_button.pack()

clear_button = tk.Button(window, text="Очистити", command=clear_canvas)
clear_button.pack()

result_label = tk.Label(window, text="")
result_label.pack()

# Список для зберігання точок, які малює користувач
drawn_points = []

def mouse_dragged(event):
    x, y = event.x, event.y
    drawn_points.append((x, y))
    canvas.create_oval(x - 3, y - 3, x + 3, y + 3, fill="black")

canvas.bind("<B1-Motion>", mouse_dragged)

window.mainloop()
