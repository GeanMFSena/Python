nome = input ('Digite seu nome: ')

print(f'Seu nome é {nome=}') 
# A função input() lê uma linha do usuário e retorna como string
# o = dentro da f-string é usado para mostrar o nome da variável e o valor dela 

variavel1 = input ('Digite um numero: ')
variavel2 = input ('Digite outro numero: ')
variavel3 = int (variavel1) + int (variavel2)   # converte as variaveis para inteiro antes de somar, caso contrário a soma será feita como string

print(f'a soma dos dois numeros é {variavel3}')

