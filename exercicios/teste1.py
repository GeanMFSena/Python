# Faca um programa que que peca ao ususario para digitar um numero inteiro,
# informe se este numero é par ou impar. caso o usuario nao digite um numero inteiro,
# informe que nao é um numero inteiro

numero_usuario = input('Por favor digite um numero:  ')




if numero_usuario.isdigit():
    usuario_int= int(numero_usuario)
    par_int = usuario_int %2 == 0
    par_impar_texto = 'impar'
    
    if par_int:
        par_impar_texto = 'par'
    
    print(f'este {usuario_int} é {par_impar_texto}')
    
else:
    print('este nao é um numero inteiro')