#Алгоритм шифрования Цезаря
#Сложность алгоритма О(n) от длины шифруемой строки
def caesar_cipher(text, shift):
    def shift_char(c, shift_amount):
        if 'a' <= c <= 'z':
            return chr((ord(c) - ord('a') + shift_amount) % 26 + ord('a'))
        elif 'A' <= c <= 'Z':
            return chr((ord(c) - ord('A') + shift_amount) % 26 + ord('A'))
        elif 'а' <= c <= 'я':
            return chr((ord(c) - ord('а') + shift_amount) % 33 + ord('а'))
        elif 'А' <= c <= 'Я':
            return chr((ord(c) - ord('А') + shift_amount) % 33 + ord('А'))
        else:
            return c

    shifted_text = ''.join(shift_char(c, shift) for c in text)
    return shifted_text


def caesar_decipher(text, shift):
    # Для дешифрования используем сдвиг в обратном направлении
    return caesar_cipher(text, -shift)


# Пример использования
text = input("Введите текст для шифрования: ")
shift = int(input("Введите величину сдвига: "))
encrypted_text = caesar_cipher(text, shift)
print(f"Зашифрованный текст: {encrypted_text}")

# Дешифрование
decrypted_text = caesar_decipher(encrypted_text, shift)
print(f"Дешифрованный текст: {decrypted_text}")
