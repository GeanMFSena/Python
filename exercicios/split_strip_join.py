frase= '     MAMXKLM akmxlkmaxlmk,         okmaxdomxsm, xmkslkxmsklmax          '

frase_dividida = frase.split(',')

lista_frases = []
for i, frase in enumerate( frase_dividida):
    lista_frases.append(frase_dividida[i].strip())

# print(lista_frases)

frases_unidas = '-'.join(lista_frases)
print(frases_unidas)

