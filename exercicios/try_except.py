# introducao a try e except
# try - tentar executar o codigo
# except - ocorreu algum erro ao tentar executar 

numero = input ('Vou dobrar o numero que voce digitar: ')


try:
    numero_float = float(numero)
    print(f'Esse é o {numero} dobrado { numero_float * 2}')

except:
    print('voce nao digitou um numero')

# if numero:
    
#     print(f'Esse é o {numero} dobrado { numero_float * 2}')
    
# else:
#     print('voce nao digitou um numero')
