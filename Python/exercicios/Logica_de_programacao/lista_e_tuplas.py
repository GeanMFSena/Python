

'''
listas(list) sao dados iteraveis e mutaveis e que colocamos uma cadeia de valores dentro dela igual a uma lista de compras ou coisas do tipo e o tipo lista sao dados que podem ser mudados diferentemente das tuplas (tuple) que sao iguais as listas guardando cadeias de valor mas com porem de serem dados imutaveis ou seja depois de criados nao podem ser alterados com outros metodos igual a lista 



'''

sla = (1 ,1, 2, 3 , 4)

mumu = [1,2,3,4,5,6]

print(sla, mumu)

# indices  0           1     2    3      4      5        6
lista = ["gean sena" , 22 , True, 2.1, ]
lista[0] = "sla".upper()
print(lista[0].upper())

numero_lista = [1,2,3,4]
numero_lista[0] = 300
del numero_lista[3]
numero_lista.append(5)
numero_lista.insert(0, 0)
numero_lista.pop()
sla = numero_lista
print(numero_lista)