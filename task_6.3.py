number_N = int(input('Enter the number "N" to create a multiplication set: '))
if number_N < 0:
    number_N *= -1

multiplier = [1]
set_product_numbers = [i for i in range(1, number_N) if multiplier.append(multiplier[i - 1] * (i + 1))]

print(f'Multiplication of numbers, from 1 to a number '
      f'{number_N} looks like this:', multiplier)