# Ввод последовательности символов
sequence = input("Enter a sequence of characters: ")

# Определение количества одинаковых символов в начале
first_char = sequence[0]  # Первый символ
count = 0

for char in sequence:
    if char == first_char:
        count += 1
    else:
        break  # Прекращаем подсчёт при первом отличном символе

# Вывод результата
print(f"Number of identical symbols at the start: {count}")
