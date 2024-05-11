


primeiro_valor=input(f'Digite um valor:  ') 
segundo_valor=input(f'Digite outro valor: ') 

if primeiro_valor == segundo_valor:
    print (f' Primeiro valor é igual que o segundo valor ' )
    
elif primeiro_valor > segundo_valor:
    print(f'{primeiro_valor=}  é maior que o {segundo_valor=}')
    
elif primeiro_valor < segundo_valor:
    print(f'{segundo_valor=} é maior que o {primeiro_valor=}')
    
else:
    print('fim')
