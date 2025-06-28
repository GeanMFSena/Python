velocidade = 61
local_carro = 100

RADAR_1 = 60
LOCAL_1 = 100
RADAR_RANGE = 1

velocidade_acima_radar = velocidade > RADAR_1

velocidade_igual_ou_menor_radar = velocidade <= RADAR_1

range_radar_multa = local_carro >= (LOCAL_1 - RADAR_RANGE) and local_carro <= (LOCAL_1 + RADAR_RANGE) 



if  range_radar_multa and velocidade_acima_radar:
    print("Carro multado")  
    
elif range_radar_multa and velocidade_igual_ou_menor_radar:
    print("Carro dentro do limite de velocidade")    

else:
     print("Carro nao multado")
