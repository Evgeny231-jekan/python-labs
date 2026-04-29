n = int(input("Введите количество школьников: "))
print()

all_languages = None
any_language = set()

for i in range(n):
    print(f"--- Школьник №{i+1} ---")
    # Считываем количество языков у текущего школьника
    m = int(input(f"  Сколько языков знает школьник №{i+1}: "))
    current_languages = set()
    
    print(f"  Введите {m} язык(а/ов) (каждый на новой строке):")
    for j in range(m):
        lang = input().strip()
        current_languages.add(lang)
        any_language.add(lang)
    
    if all_languages is None:
        all_languages = current_languages.copy()
    else:
        all_languages &= current_languages
    print()

# Выводим результаты
print("=" * 40)
print("РЕЗУЛЬТАТЫ:")
print("=" * 40)

# Выводим языки, которые знают все
print(f"Количество языков, которые знают ВСЕ школьники: {len(all_languages)}")
if len(all_languages) > 0:
    print("Список этих языков (в алфавитном порядке):")
    for lang in sorted(all_languages):
        print(f"  • {lang}")
else:
    print("  (нет общих языков)")
print()

# Выводим языки, которые знает хотя бы один
print(f"Количество языков, которые знает ХОТЯ БЫ ОДИН школьник: {len(any_language)}")
print("Список этих языков (в алфавитном порядке):")
for lang in sorted(any_language):
    print(f"  • {lang}")
