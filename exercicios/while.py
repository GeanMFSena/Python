
condicao = True

while condicao:
    nome = input("Digite o seu nome (ou digite 'sair' para encerrar): ")
    print(f"O nome que você digitou é: {nome}")
    
    if nome == 'sair':
        print('Voce saiu do programa')
        break
        
    