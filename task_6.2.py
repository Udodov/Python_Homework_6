numbers = list()
numbers_list = [i for i in range(5) if numbers.append(int(input(f'Enter a number № {i + 1} -->')))]
print(numbers)

maximum = numbers[0]

for i in range(1, len(numbers)):
    if numbers[i] > maximum:
        maximum = numbers[i]

print('Maximum number = ', maximum)
