def read_numbers(filename):
    f = open(filename, 'r')
    content = f.read().strip()
    f.close()
    if content == '':
        return []
    numbers = []
    for x in content.split():
        numbers.append(int(x))
    return numbers

def write_numbers(filename, numbers):
    f = open(filename, 'w')
    for i in range(len(numbers)):
        if i > 0:
            f.write(' ')
        f.write(str(numbers[i]))
    f.close()

def transform_array(arr):
    n = len(arr)
    result = []
    left = 0
    right = n - 1
    
    while left <= right:
        if left == right:
            result.append(arr[left])
            break
        result.append(arr[left])
        result.append(arr[right])
        left = left + 1
        right = right - 1
    
    return result

input_file = "input.txt"
output_file = "output.txt"

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
f = open(input_file, 'w')
for i in range(len(numbers)):
    if i > 0:
        f.write(' ')
    f.write(str(numbers[i]))
f.close()

data = read_numbers(input_file)
transformed = transform_array(data)
write_numbers(output_file, transformed)

print("Исходные числа:", data)
print("Преобразованные числа:", transformed)
