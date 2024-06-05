

while  True:
    primeiro_numero= input ('insira um numero:  ')
    segundo_numero = input ('insira um segundo numero:  ')
    operador = input ( 'insira um operador "so aceitamos +, -, / , * :  "')
    
    numero_validos= None

    
    
    try:
        primeiro_numero_int = float ( primeiro_numero)
        segundo_numero_int = float ( segundo_numero)
        numero_validos = True

            
    except:
        numero_validos =None    
        
    if numero_validos is None:
            print('O numero que voce digitou é invalido')
            continue
        
    operadores_permitidos= '+-/*'
        
    if operador not in operadores_permitidos:
            print('Digite um operador valido')
            continue
        
    if len(operador) > 1:
            print('digite apenas um operador')
            continue
        
    print('O valor é')
        
    if operador == '+' :
           print(segundo_numero_int + primeiro_numero_int)
    elif operador == '-' :
            print(segundo_numero_int - primeiro_numero_int)
    elif operador == '/' :
            print  (segundo_numero_int / primeiro_numero_int)
    elif operador == '*' :
            print  (segundo_numero_int * primeiro_numero_int)
        
    
    sair = input('Se voce quiser sair digite [s]air: ').lower().startswith('s')
    if sair == True:
            break