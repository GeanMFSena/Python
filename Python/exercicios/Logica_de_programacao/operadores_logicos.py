# Exercício: Operadores Lógicos AND e OR

entrar_ou_sair = input("Digite [E]ntrar ou [S]air: ")
verificar_senha = input("Digite a sua senha: ")
senha = "123456"



if (entrar_ou_sair == "E" or entrar_ou_sair == "e")  and verificar_senha == senha:
    print("Você entrou no sistema.")
elif entrar_ou_sair == "S" or entrar_ou_sair == "s":
    print("Você saiu do sistema.")
else:
    print("Voce nao digitou uma opçao valida [E]ntrar /[S]air ou senha esta incorreta.")


# Exercício: Operadores Lógicos IN e NOT IN  

algum_texto = input("Digite algum texto:  ")
procurar = input("Digite o que deseja procurar:  ")


if procurar in algum_texto:
    print(f"voce digitou = {procurar} essa palavra ou texto existe no {algum_texto} ")
else:
    print(f" O texto digitado nao esta dentro de {algum_texto=}")
    


algum_texto = input("Digite algum texto:  ")
procurar = input("Digite o que deseja procurar:  ")


if procurar not in algum_texto:
    print(f"voce digitou = {procurar} essa palavra ou texto nao existe no {algum_texto} ")
else:
    print(f" O texto digitado esta dentro de {algum_texto=}")


    






