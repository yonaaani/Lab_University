def generate_key_table(keyword, k):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    keyword = keyword.upper()
    key_table = list(keyword)
    
    for char in alphabet:
        if char not in key_table:
            key_table.append(char)
    
    key_table = key_table[-k:] + key_table[:-k]
    
    return ''.join(key_table)

def affine_caesar_cipher(plaintext, key_table):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    ciphertext = ''

    for char in plaintext:
        if char.isalpha():
            index = alphabet.index(char.upper())
            encrypted_char = key_table[index]
            if char.islower():
                encrypted_char = encrypted_char.lower()
            ciphertext += encrypted_char
        else:
            ciphertext += char
    
    return ciphertext

def main():
    # Зчитуємо відкрите повідомлення з файлу
    with open(r"C:\Users\yonaaani\OneDrive\Рабочий стол\lab3\text1.txt", 'r') as file:
        plaintext = file.read()

    # Вводимо ключове слово та число k з клавіатури
    keyword = input("Введіть ключове слово: ").upper()
    k = int(input("Введіть число k (0 < k < 25): "))
    
    # Генерація таблиці ключа
    key_table = generate_key_table(keyword, k)
    print("Таблиця ключа:", key_table)

    # Шифруємо повідомлення та зберігаємо шифрограму у файл
    ciphertext = affine_caesar_cipher(plaintext, key_table)
    
    with open(r"C:\Users\yonaaani\OneDrive\Рабочий стол\lab3\criphertext1.txt", 'w') as file:
        file.write(ciphertext)

    print("Шифрування завершено. Результат збережено у файлі criphertext1.txt")

if __name__ == "__main__":
    main()
