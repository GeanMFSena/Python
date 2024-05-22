# Exercicio

# Peça ao usuario para colocar o nome
# Peça ao usuario para colocar a idade

# se o nome e a idade forem digitados exiba:
#     seu nome é {nome}
#     seu nome invertido é {nome invertido}
#     se o nome contem ou nao espacos
#     se o nome tem {n} nas letras
#     a primeira letra do seu nome é { letra}
#     a ultima letra do seu nome é {letra}
    
#     se nada for exibido nos campos mostre: 'desculpe vc nao digitou nada nos campos'



nome= input('Insira seu nome: ')
idade= input('Insira sua idade: ')

if nome and idade:
    print(f"seu nome é {nome} e voce tem {idade} anos")
    print(f'Seu nome invertido é ',{nome[::-1]})
    
    
    if " " in nome  :
        print("Seu nome contem espacos")
        
    
    else:
        print('Seu nome nao contem espacos')    
    
    
    
    print(f'Seu {nome=} contem uma quantidade de letras de : ',len(nome))
    print(f'A primeira letra do seu nome é ',{nome[0]})
    print(f'A ultima letra do seu nome é ',{nome[-1]})
    
    
    
    
else:
    print('desculpe vc nao digitou nada nos campos')