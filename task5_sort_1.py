def sort_by_word_count(strings):
    """Сортирует строки по количеству слов"""
    return sorted(strings, key=lambda s: len(s.split()))


print("Введите строки (для завершения введите пустую строку):")
strings = []
while True:
    line = input()
    if line == "":
        break
    strings.append(line)

if strings:
    sorted_strings = sort_by_word_count(strings)
    print("\nИсходный список:")
    for s in strings:
        print(f"  '{s}' (слов: {len(s.split())})")
    print("\nОтсортировано по количеству слов:")
    for s in sorted_strings:
        print(f"  '{s}' (слов: {len(s.split())})")
else:
    print("Список пуст")
