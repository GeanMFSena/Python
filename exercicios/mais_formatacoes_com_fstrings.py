# Formatacao basica de strings 
# s - Strign
# d e i - int
# f - float 
# .<numero de digitos>f
# x ou X  - Hexadecimal

# (Caractere )(><^)(Quantidade)

# > - Esquerda 
# < - Direita 
# ^ -  Centro
# Sinal - + ou -
# = - força o numero a aparecer antes dos zeros
# Ex.: 0>-100,.1f
# Conversion flags -  !r !s !a



variavel = "abc"
variavel2 =float('1219209.00121') 
print(f"{variavel: >10}" )
print(f"{variavel: <10}")
print(f"{variavel: ^10}" )
print(f"{variavel2:>=+000,.2f}")
print(f'O numero hexadecimal de 2000 é: {2000: 04X}')

