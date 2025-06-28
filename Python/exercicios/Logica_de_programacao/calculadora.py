while True: 
    primeiro_numero = input("Digite o primeiro numero:  ")
    segundo_numero = input("Digite o segundo numero:  ")
    operador = input("Digite o operador (+, -, *, /):  ")

    try:
        float_primeiro_numero = float(primeiro_numero)
        float_segundo_numero = float(segundo_numero)
        
        if operador == "+":
            print(f"a soma dos dois numeros é {float_primeiro_numero + float_segundo_numero}")
            
        elif operador == "-":
            print(f"a subtraçao dos dois numeros é {float_primeiro_numero - float_segundo_numero}")
        
        elif operador == "*":
            print(f"a multiplicaçao dos dois numeros é {float_primeiro_numero * float_segundo_numero}")
        
        elif operador == "/":
            print(f"a divisao dos dois numeros é {float_primeiro_numero / float_segundo_numero}")
        
        else:
            print("nao reconheço esse operador, por favor digite um operador valido (+, -, *, /).")
            continue

        sair_ou_nao = input ("Deseja sair do programa? [s]im ou [n]ao :  ").lower().startswith("s")
        
        if sair_ou_nao == True:
            print("Obrigado por usar a calculadora, ate mais!")
            break        
        
        elif sair_ou_nao == False:
            print("Coloque os proximos numeros")
            continue
        
    except:
        print("ocorreu um erro, por favor digite os numeros e o operador corretamente.")
        continue    
        
        

