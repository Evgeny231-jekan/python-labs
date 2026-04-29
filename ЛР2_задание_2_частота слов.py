

n = int(input("Введите количество строк в тексте: "))
print(f"Теперь введите {n} строк(и/у) текста (каждую с новой строки):")
print("-" * 40)

freq = {}

for line_num in range(1, n + 1):
    line = input().strip()
    if line:  
        words = line.split()
        for word in words:
            freq[word] = freq.get(word, 0) + 1

print()
print("=" * 40)
print("РЕЗУЛЬТАТЫ ЧАСТОТНОГО АНАЛИЗА:")
print("=" * 40)


items = [(-count, word) for word, count in freq.items()]
items.sort()  


print("Слова в порядке убывания частоты встречаемости:")
print("-" * 40)
for _, word in items:
    print(f"  {word}")


