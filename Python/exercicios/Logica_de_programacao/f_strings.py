nome = 'Gean'
idade = 22 
altura = 1.70
peso = 73.00
imc = peso / (altura ** 2)


texto = f'{nome} tem {altura} pesa {peso} KG e seu IMC é {imc:.2f}'


print(f'{nome} tem {altura:.2f} pesa {peso:.2f} KG e seu IMC é {imc:.2f}')

print(f'Seu nome é {nome=}') # o = dentro da f-string é usado para mostrar o nome da variável e o valor dela 



# Formatacao basica de strings 
# s - Strign
# d e i - int
# f - float 
# .<numero de digitos>f
# x ou X  - Hexadecimal

# (Caractere )(><^)(Quantidade)

# > - Esquerda 
# < - Direita 
# ^ -  Centro
# Sinal - + ou -
# Ex.: 0>-100,.1f
# Conversion flags -  !r !s !a
# Para trazer o nome e o valor de uma variavel dentro de algo usando f-strings coloque
# o nome da variavel dentro das chaves {} e depois coloque um sinal de = na frente da variavel
# se voce quiser adicionar espaçamento ou algum caractere de preenchimento antes do nome da variavel ou depois voce pode usar o seguinte formato: ( Caractere que podem ser varios tipos pois quase todos sao aceitos ) (><^ simbolos para adicionar a esquerda, direita e centro) (Quantidade)

#exemplo: 
# variavel = "ABC"
# print(f"{variavel: >10}") # adiciona 10 espaços a esquerda
# print(f"{variavel: <10}") # adiciona 10 espaços a direita
# print(f"{variavel: ^10}") # adiciona 10 espaços no centro
# print(f"{variavel:!^10}") # adiciona 10 espaços no centro e preenche com o caractere !

nome = "Gean"
variavel = "ABC"
numero_para_hexadecimal = 255

print(f"{variavel: >10}") # adiciona 10 espaços a esquerda
print(f"{variavel: <10}") # adiciona 10 espaços a direita
print(f"{variavel: ^10}") # adiciona 10 espaços no centro
print(f"{variavel:!^10}") # adiciona 10 espaços no centro e preenche com o caractere !

numero = 123456.78910

print(f"{numero:.1f}") # formata o numero para 1 casas decimais

print(f"Ola {nome} o hexadecimal de {numero_para_hexadecimal} é {numero_para_hexadecimal:04X}") # formatando numero para hexadecimal com 4 digitos