import decimal



numero = decimal.Decimal("0.1") 
numero2 = decimal.Decimal("0.7")
numero3 = decimal.Decimal(numero + numero2)
print(numero3)
print(f"{numero3:.2f}")
print(round(numero3, 2))
