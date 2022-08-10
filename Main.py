import random

digits = [random.randint(0, 25) for count in range(0, 4)]
aver = sum(digits) / len(digits)

print('Числа: ' + ', '.join(str(digit) for digit in digits))
print('Среднее арифметическое: ', aver, '\n')
def factor(x):
    if x == 0:
        return 1
    return factor(x - 1) * x

for digit in digits:
    print('Факториал числа', digit, '\t:', factor(digit))
