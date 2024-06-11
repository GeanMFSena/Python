import sys


entrada_cpf = input('Digite o seu cpf: ').replace('.', '')\
    .replace('-', '')\
    .replace(' ', '')
    
    
    
    
entrada_sequencial = entrada_cpf == entrada_cpf[0] * len(entrada_cpf) 
    
if entrada_sequencial:
    print('Voce enviou dados sequenciais')
    sys.exit
    
    
nove_digitos = entrada_cpf[0:9]
contagem_regressiva_1 = 10


resultado_dig_1 = 0
for digito_1 in nove_digitos:
    
    resultado_dig_1 += int(digito_1) * contagem_regressiva_1
    contagem_regressiva_1 -= 1
    
digito_1 = (resultado_dig_1 * 10) % 11
digito_1 = digito_1 if digito_1 <= 9 else 0

        
        
        
        
segundo_digito =  entrada_cpf [0:10]   
contagem_regressiva_2 = 11


resultado_dig_2 = 0
for digito_2 in segundo_digito:
    
    resultado_dig_2 += int(digito_2) * contagem_regressiva_2
    contagem_regressiva_2 -= 1
    
digito_2 = (resultado_dig_2* 10) % 11
digito_2 = digito_2 if digito_2 <= 9 else 0
calculo_ger = f'{nove_digitos}{digito_1}{digito_2}'

if calculo_ger == entrada_cpf:
    print(calculo_ger, 'cpf valido')
else:
    print('cpf invalido')