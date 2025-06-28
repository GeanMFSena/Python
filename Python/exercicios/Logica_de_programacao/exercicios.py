
try: 
    int_usuario_digitado = int(input("Digite um numero inteiro:  "))
    
    if int_usuario_digitado % 2 == 0:
        print(f"o numero digitado {int_usuario_digitado} é par")
    
    elif int_usuario_digitado % 2 != 0:
        print(f"O numero digitado {int_usuario_digitado} é impar")


except ValueError:
    print("O valor digitado nao é um numero inteiro, por favor digite um numero inteiro valido.")
    

try:
    hora_usuario_digitado = input("Digite a hora atual em numeros inteiros por favor:  ")
    hora_usuario_digitado_int = int(hora_usuario_digitado)
    
    if hora_usuario_digitado_int  > 0 and hora_usuario_digitado_int < 12:
        print(f"As horas que voce digitou foram {hora_usuario_digitado_int} bom dia")
    elif  hora_usuario_digitado_int > 11 and hora_usuario_digitado_int < 18 :
        print(f"As horas que voce digitou foram {hora_usuario_digitado_int} boa tarde")
    elif  hora_usuario_digitado_int > 17 and hora_usuario_digitado_int < 24 :
        print(f"As horas que voce digitou foram {hora_usuario_digitado_int} boa noite")
    else:
        print("O valor digitado nao é um horario valido, por favor digite um horario valido entre 0 e 23 horas.")

except:
    print("O valor digitado nao é um horario valido, por favor digite um horario valido entre 0 e 23 horas.")



try:
    nome = input("Digite o seu nome:  ")   
    tamanho_do_nome = len(nome)    
    
    if tamanho_do_nome > 1:
        if tamanho_do_nome <= 4 :
            print(f"Seu nome {nome} é curto")
        
        elif tamanho_do_nome >= 5 and tamanho_do_nome <= 6 :
            print(f"seu nome {nome} é normal")
        
        else:
            print(f"Seu nome {nome} é longo")       
    else:
        print("digite mais de uma letra por favor")    
except:
    print(f"Seu nome nao é um valor ou nome valido, por favor digite um nome valido.")