import socket
import hashlib

# Опреділяємо параметри для генерації хешу
salt = b'salt_value'  # Сіль для унікальності генерованого хешу
iterations = 100000  # Кількість ітерацій для PBKDF2

# Створення хеша пароля
def hash_password(password):
    return hashlib.pbkdf2_hmac('sha256', password.encode(), salt, iterations)

# Створення файлу з паролями та їх хешами
with open('C:/Users/yonaaani/OneDrive/Рабочий стол/lab8/security_token.txt', 'w') as file:
    username = input("Enter username: ")
    password = input("Enter password: ")
    file.write(f"{username}|{hash_password(password).hex()}\n")

# Перевірка паролю
def verify_password(token_data, username, password):
    stored_username, stored_password_hash = token_data.split('|')
    if username == stored_username:
        key = hash_password(password)
        return key.hex() == stored_password_hash.strip()  # Видаляємо символ нового рядка з кінця рядка
    return False

# Створюється TCP-сокет, який прослуховує з'єднання на локальній адресі 127.0.0.1 і порту 12345
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('127.0.0.1', 12345))
server_socket.listen(1)

print("Server is listening...")

# Отримання даних з файлу на токені безпеки
with open('C:/Users/yonaaani/OneDrive/Рабочий стол/lab8/security_token.txt', 'r') as file:
    token_data = file.readline()  # Читаємо лише перший рядок файлу

while True:
    client_socket, client_address = server_socket.accept()
    print(f"Connection from {client_address} has been established.")

    # Отримання даних з клієнта
    data = client_socket.recv(1024)
    username, password = data.decode().split('|')

    # Перевірка паролю
    if verify_password(token_data, username, password):
        client_socket.send(b"Authentication successful.")
    else:
        client_socket.send(b"Authentication failed.")

    client_socket.close()
