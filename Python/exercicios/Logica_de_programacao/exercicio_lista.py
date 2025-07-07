




lista = [] 
 
    
while True:
    
        usuario_digitado = input("Digite uma das seguintes opçoes: [i]nserir ou [a]pagar ou [l]istar ").lower()

        try:           

                if  usuario_digitado == "i":
                        opçao_objeto = input("Digite o que deseja adicionar: ")
                        lista.append(opçao_objeto)
                        for lista_numerada, objetos_lista in enumerate(lista):
                                print(f"Agora na lista temos os seguintes objetos :{objetos_lista}")
                


                elif usuario_digitado == "l" and len(lista) == 0 :
                        print("A lista esta vazia por favor adicione algo antes de listar")
                                
                elif usuario_digitado == "l":
                     for lista_numerada, objetos_lista in enumerate(lista):
                        print(f"indice: {lista_numerada} e objeto: {objetos_lista}")

                                                
                elif usuario_digitado == "a":
                        opçao_objeto = input("Digite o indice que deseja apagar: ")
                        int_opçao_objeto = int(opçao_objeto)
                        del lista[int_opçao_objeto]
                        print(lista)
                
                else:
                        print("Por favor digite uma das opçoes a seguir: [i]nserir [a]pagar [l]istar ")
                
                        
        except:
                print("Voce tentou apagar indices que nao existem na lista")
                
                                
