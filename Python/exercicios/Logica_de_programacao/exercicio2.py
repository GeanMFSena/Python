primeiro_valor = input("Digite o primeiro valor: ")
segundo_valor = input("Digite o segundo valor: ") 

primeiro_valor_int = int(primeiro_valor)
segundo_valor_int = int(segundo_valor)  

if primeiro_valor_int > segundo_valor_int: 
    print(f"{primeiro_valor_int=} é maior que o segundo valor {segundo_valor_int=}")
    
elif primeiro_valor_int == segundo_valor_int:
    print(f"{primeiro_valor_int=} é igual ao segundo valor {segundo_valor_int=}")
     
else:
    print(f"{segundo_valor_int=} é maior que o primeiro valor {primeiro_valor_int=} ")   
