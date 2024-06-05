
lista = []

while True:

    usuario = input('Selecione uma opcao das opcoes: [i]nserir [a]pagar [l]istar ')
    
    
    if usuario == 'i':
       usuario_digitado = input('Digite o que deseja adicionar a lista: ')
       continue
   
    
    
    if usuario == 'l':
        
        lista.append(usuario_digitado)
        for indice, item in enumerate (lista):
            print(indice, item)
            
        
    if usuario == 'a':
       usuario_del = input(f'digite o indice que deseja apagar: ') 
       usuario_del_int = int(usuario_del)
       lista.pop(usuario_del_int)
        
        
    else:
        print('Voce nao Digitou nehuma funcacao por favor digite i, a ou l.')                 
         
