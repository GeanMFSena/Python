frase =  "Python é uma linguagem de programaçao multiparadigma. Python foi criado por Guido van Rossum"


i = 0 


qtd_letra_apareceu_mais_vezes = 0 
letra_apareceu_mais_vezes = ""


while i < len(frase):
    letra_atual = frase[i]
    qtd_letras = frase.count(letra_atual)
    
    
    if letra_atual == " ": 
        i += 1
        continue
    
    if qtd_letra_apareceu_mais_vezes < qtd_letras:
        qtd_letra_apareceu_mais_vezes = qtd_letras
        letra_apareceu_mais_vezes = letra_atual
    i += 1    
        
print(f"{letra_apareceu_mais_vezes} apareceu {qtd_letra_apareceu_mais_vezes}")
    
    

    

    