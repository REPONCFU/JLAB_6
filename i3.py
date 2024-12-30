# Ввод предложения
sentence = input("Enter a sentence: ")

# Ввод индексов n1 и n2
n1 = int(input("Enter the starting index (n1): "))
n2 = int(input("Enter the ending index (n2): "))

# Удаление символов с n1-го по n2-й (включительно)
result = sentence[:n1] + sentence[n2 + 1:]

# Вывод результата
print(f"Modified sentence: {result}")
