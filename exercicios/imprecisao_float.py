import decimal



num = decimal.Decimal('0.1')
num2 = decimal.Decimal('0.7')
num3 = num + num2
print(f'{num3:.2f}')
print(round(num3, 2))
print(num3)