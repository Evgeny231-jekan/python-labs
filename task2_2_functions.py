def lowercase_latin_palindrome(s):
    """Проверяет, образуют ли строчные латинские буквы палиндром"""
    letters = [ch for ch in s if ch.islower() and ch.isalpha() and 'a' <= ch <= 'z']
    return letters == letters[::-1]


text = input("Введите строку: ")
result = lowercase_latin_palindrome(text)
print(f"Строчные латинские буквы образуют палиндром: {result}")
if result:
    letters = [ch for ch in text if ch.islower() and ch.isalpha() and 'a' <= ch <= 'z']
    print(f"Найденные буквы: {''.join(letters)}")
