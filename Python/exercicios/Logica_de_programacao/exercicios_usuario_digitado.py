nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")


if nome and idade:
    print(f"Seu nome é {nome}")
    print(f"seu nome invertido é {nome[::-1]}")
    if " " in nome: 
        print("seu nome contem espacos")
    else:
        print("Seu nome não contem espacos")
    print(f"seu nome tem {len(nome)} letras")
    print(f"a primeira letra do seu nome é {nome[0:1]}")
    print(f"á ultima letra do seu nome é {nome[-1]}")
    
else: 
    print("Desculpe, mas voce deixou campos em branco")