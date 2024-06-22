a = 1000

def funcao():
    a = 11000
    b = 'sexo'
    def outra_funcao():
        a = 'anao de jardim'
        b = 'minhas bolas'
        print(a, b)    
    outra_funcao()
    print(b,a)

print(a)    
funcao()
print(a)
