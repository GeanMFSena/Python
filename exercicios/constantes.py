# CONSTANTES = "variaveis" que nao vao mudar 
# Muitas condicoes no mesmo if (ruim)
#     Muita complexidade (ruim)

velocidade = 60
km_do_carro = 90 

VEL_MAXIMA_RADAR = 60
LOCALIZACAO_KM_RADAR = 100
RANGE_RADAR = 1


if velocidade > VEL_MAXIMA_RADAR:
    print('Voce passou da velociade maxima')
    
else: 
    print('Voce nao ultrapassou a velocidade')