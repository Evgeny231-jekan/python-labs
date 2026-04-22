def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def sum_of_prime_divisors(num):
    divisors = []
    for i in range(2, abs(num) + 1):
        if num % i == 0 and is_prime(i):
            divisors.append(i)
    return sum(divisors)
n = int(input("Введите число:"))
print(sum_of_prime_divisors(n))

def count_odd_digits_greater_than_3(num):
    count = 0
    for ch in str(abs(num)):
        digit = int(ch)
        if digit % 2 != 0 and digit > 3:
            count += 1
    return count
m = int(input("Введите число:"))
print(count_odd_digits_greater_than_3(m))

def digit_sum(n):
    return sum(int(d) for d in str(abs(n)))

def product_of_divisors_with_digit_sum_less_than_original(num):
    original_digit_sum = digit_sum(num)
    product = 1
    found = False
    for i in range(1, abs(num) + 1):
        if num % i == 0 and digit_sum(i) < original_digit_sum:
            product *= i
            found = True
    return product if found else 0
n = int(input("Введите число:"))
print(product_of_divisors_with_digit_sum_less_than_original(n))
