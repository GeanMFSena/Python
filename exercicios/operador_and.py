
#1• Operadores •lógicos

#2• and • (e) • or • (ou) • not • (não)

#3• and • - • Todas• as • condições precisam ser verdadeiras.

#5•Se qualquer valor for considerado falso,

#6•a • expressão inteira será avaliada naquele valor

#7• São considerados false (que •vc • já viu)

#8• 0•0.0.''• False

#9• Também • existe o tipo None que • é usado-para • representar - um •nao-valor


entrada = input(f'[E]ntrar e [S]air: ')
print(entrada)

senha_digitada= input(f'Digite sua senha: ')
senhalegal = int('123456')



if entrada == 'E' or entrada == 'e' and senhalegal == senha_digitada  :
    print('Entrar')


else :
    print('Sair')
    
    

x = 5
y = 10

# Verifica se x é maior que 3 ou y é menor que 5
if x > 3 or y < 5:
    print("Pelo menos uma das condições é verdadeira.")
else:
    print("Ambas as condições são falsas.")