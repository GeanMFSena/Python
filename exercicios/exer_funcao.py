def multiplica_argumentos (*args):
    mult = 1
    for numeros in args:
        mult *= numeros

    
    return mult

resultado = multiplica_argumentos (1,2,3,4,5,6,7,8,9,10)
print ( resultado)

def par_ou_impar(*args):
    
    for numeros in args:
        
        if numeros % 2 == 0:
            print(f'numero par')
            
        if numeros % 2 == 1:
            print(f'numero impar')
    return 
    
par_ou_impar (5,9,901283903,90,12031,0,7,8,9,10)
valores = par_ou_impar 
   
        
# valor = 10, 11

# for numeros in valor :
#     if numeros % 2 == 0:
#         print('este numero é par',)
    
#     elif numeros % 2 == 1:
#         print('estes numeros sao impares', )
    

