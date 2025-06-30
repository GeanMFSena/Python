import os


palavra_secreta = "arroz"

letra_acertadas = ""
tentativas = 0 


while True:

    
        
            letra_digitada = input("Digite uma letra: ").lower()
            
            if  letra_digitada in palavra_secreta and len(letra_digitada) == 1: 
                        print(f"a letra digitada foi '{letra_digitada}' , digite a proxima letra")
                        tentativas += 1 
                        letra_acertadas += letra_digitada
                        
            elif len(letra_digitada) > 1:
                print("Digite apenas uma letra")
                continue
            
            palavra_formada = ""    
            
            
            for letra_secreta in palavra_secreta:
                if letra_secreta in letra_acertadas:        
                        palavra_formada += letra_secreta
                else:
                    palavra_formada += "*"
            print(palavra_formada)
            
            if palavra_formada == palavra_secreta:
                os.system('cls')
                print(f"Voce acertou a palavra secreta '{palavra_secreta}', parabens! o seu numero de tentativas foi de: {tentativas}")
                break
        
