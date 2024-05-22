# Interpolacao basica de string 

# %s - Strign
# % d e i - int
# %f - float 
# % x(Retorna os dados em minusculo) e X (Retorna dos dados em maiusculo) - Hexadecimal (ABCDEF123456789)




nome = 'gena' 
preco = float('10020.3030')
precodacompra = ('%s pagou RS%.2f no produto' %(nome, preco) ) 
hexadecimal = 15


print(precodacompra)
print( "o valor exadecimal de %d é: %x" %( 132034 , 132034 ) )
