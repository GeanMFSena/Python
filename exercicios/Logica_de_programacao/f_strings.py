nome = 'Gean'
idade = 22 
altura = 1.70
peso = 73.00
imc = peso / (altura ** 2)


texto = f'{nome} tem {altura} pesa {peso} KG e seu IMC é {imc:.2f}'


print(f'{nome} tem {altura:.2f} pesa {peso:.2f} KG e seu IMC é {imc:.2f}')

print(f'Seu nome é {nome=}') # o = dentro da f-string é usado para mostrar o nome da variável e o valor dela 