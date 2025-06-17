# fatiamento de strings

#  0  1  2  3  4  5  6  7  8
#  o  l  a ()  m  u  n  d  o ( tem um espaco dentro que tambem é considerado um caracter)
# -9 -8 -7 -6 -5 -4 -3 -2 -1
# fatiamento [f:i:p] [::]
# obs: a funcao len retorna a quantidade de caracteres que um obejeto tem como uma str int etc

nome = "Gean"
sobrenome = "Sena"
ola_mundo = "ola mundo"

print(len(nome))  # Retorna a quantidade de caracteres que a string tem

print(f"Ola meu nome é {nome[0:5]} e o meu sobrenome é {sobrenome[0:]} ") 

print("Ola meu nome é %s e o meu sobrenome é %s" % (nome, sobrenome))  # Usando o operador % para formatar a string

print(f"Ola meu nome é {nome[0:5:2]} e o meu sobrenome é {sobrenome[0:]} ") 


print(ola_mundo[0:len(ola_mundo):2])  # Fatiamento de string com passo de 2

print(ola_mundo[-1:-10:-1])  