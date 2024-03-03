def encrypt(text, a, b, m):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            if char.isupper():
                encrypted_text += chr((a * (ord(char) - 65) + b) % m + 65)
            else:
                encrypted_text += chr((a * (ord(char) - 97) + b) % m + 97)
        else:
            encrypted_text += char
    return encrypted_text

def main():
    input_file_path = r"C:\Users\yonaaani\OneDrive\Рабочий стол\lab3\text.txt"
    output_file_path = r"C:\Users\yonaaani\OneDrive\Рабочий стол\lab3\criphertext.txt"
    a = int(input("Введіть значення 'a' для афінної системи: "))
    b = int(input("Введіть значення 'b' для афінної системи: "))
    m = 26  # Для алфавіту з 26 літерами

    with open(input_file_path, 'r') as file:
        plaintext = file.read()

    encrypted_text = encrypt(plaintext, a, b, m)

    with open(output_file_path, 'w') as file:
        file.write(encrypted_text)

    print("Шифрування завершено. Шифрограма збережена в", output_file_path)

if __name__ == "__main__":
    main()
