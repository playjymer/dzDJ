def is_palindrome(s):
    return s == s[::-1]

# Пример использования
string1 = "лепсспел"
print(is_palindrome(string1))  # Вывод: True

string2 = "helloworld"
print(is_palindrome(string2))  # Вывод: False