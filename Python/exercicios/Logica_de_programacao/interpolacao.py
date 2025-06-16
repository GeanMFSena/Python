'''
Interpolação de strings em Python
Interpolação de strings é o processo de inserir valores em uma string, substituindo marcadores ou variáveis por seus valores correspondentes. Em Python, isso pode ser feito de várias maneiras, incluindo o uso de f-strings (Python 3.6+), o método `str.format()`, e a formatação antiga com o operador `%`.

s - String
d e i  - int ou Inteiro
f - float ou ponto flutuante
x ou X - Hexadecimal

se for utilizar a interpolaçao dentro do print coloque os parametros dentro do print


para adicionar zeros a esquerda utilize %04X ou %04d, onde 04 é o tamanho total da string e X ou d é o tipo de dado (hexadecimal ou inteiro).

exemplo:
variavel2 =  "Ola %s o hexadecimal de %i é %04X " % (nome, 255, 255)

resultado:
Ola Gean o hexadecimal de 00255 é 00FF 

'''

nome = "Gean"
preco = 10000.0075
variavel = "Ola %s o preco do carro é %.2f reais" % (nome, preco)
print("Ola %s o preco do carro é %.2f reais" % (nome, preco))

variavel2 =  "Ola %s o hexadecimal de %i é %04X " % (nome, 255, 255)

print(variavel2)