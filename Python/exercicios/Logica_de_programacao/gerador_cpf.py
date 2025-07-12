 #  29099278063    71053133073

'''

2 * 10 = 20 
9 * 9 = 81
0 * 8 = 0
9 * 7 = 63
9 * 6 = 54
2 * 5 = 10
7 * 4 = 28
8 * 3 = 24
0 * 2 = 0

'''


cpf = input("digite o seu cpf: ") 

cpf = cpf.replace(".", "").replace("-","")

nove_digitos = cpf[:9]

soma_primeiro_digito = 0 
reduçao1 = 10




while True:
    
        
        
        for numeros in nove_digitos: 
            numeros = int(numeros)
            multiplicar = numeros * reduçao1
            reduçao1 -= 1
            print(multiplicar)
            soma_primeiro_digito += multiplicar
        break    


calculo_primeiro_digito = (soma_primeiro_digito * 10) % 11  

primero_digito = calculo_primeiro_digito if calculo_primeiro_digito <= 9 else 0

print(f"o resto da divisao do primeiro digito é {primero_digito}")


dez_digitos = cpf[:10]

soma_segundo_digito = 0 
reduçao2 = 11

while True:
    for numeros_2_digito in dez_digitos: 
        numeros_2_digito = int(numeros_2_digito)
        multiplicar_2_digito = numeros_2_digito * reduçao2
        reduçao2 -= 1
        print(multiplicar_2_digito)
        soma_segundo_digito += multiplicar_2_digito
    break    


calculo_segundo_digito = (soma_segundo_digito * 10) % 11  
segundo_digito = calculo_segundo_digito if calculo_segundo_digito <= 9 else 0

print(f"o resto da divisao do segundo digito é {segundo_digito}")


novo_cpf = nove_digitos + str(primero_digito) + str(segundo_digito)

if novo_cpf == cpf :
    print(f"o cpf {cpf} é valido")
else:
    print(f"cpf invalido")
    
    
