import math

def listaFuncao(n):
    if  n ==1:
        return lambda x: ((x**3)-9*x+3)
    if n == 2:
        return lambda x: math.cos(x)-x
    if n == 3:
        return lambda x: (x**2)+x-6
    
def listaDerivadaFuncao(n):
    if n == 1:
        return lambda x: ((3*(x**2))-9)
    if n == 2:
        return lambda x: -math.sin(x)-1
    if n == 3:
        return lambda x: (2*x)+1

funcao = int(input("digite o nr da funcao: "))
f = listaFuncao(funcao)
df = listaDerivadaFuncao(funcao) 

a = float(input("limite inferior: "))
b = float(input("limite superior: "))
x0 = float(input("Aproximacao inicial: "))

antigo_valor = []
antigo_valor.append(a)
antigo_valor.append(b)
antigo_valor.append(x0)

x = ['Iteracao', 'a', 'b', 'f(a)', 'f(b)', 'x', 'f(x)']
sep = ['--------', '-----------', '-----------', '-----------', '-----------', '-----------', '-----------']
print('{:^141}'.format('METODO DA BISSECAO'))
print('')
print('{:<10}  {:<20}  {:<20}  {:<25}  {:<25}  {:<20}  {:<21}'.format(*x))
print('{0:<10}  {0:<20}  {0:<20}  {0:<25}  {0:<25}  {0:<20}  {0:<21}'.format(*sep))
anterior = 0
cont = 1
while True:
    linha = []
    linha.append(cont)
    linha.append(a)
    linha.append(b)
    funcao_a = f(a)
    funcao_b = f(b)
    r_aprox = (a+b)/2
    funcao_x = f(r_aprox)
    linha.append(funcao_a)
    linha.append(funcao_b)
    linha.append(r_aprox)
    linha.append(funcao_x)
    if anterior == r_aprox:
        for i in range(30):
            print('{:<10}  {:<20}  {:<20}  {:<25}  {:<25}  {:<20}  {:<21}'.format(*linha))
            cont += 1
            linha[0] = cont
        break
    if funcao_a*funcao_x > 0:
        a = r_aprox
    else:
        b = r_aprox
    anterior = r_aprox
    cont += 1
    print('{:<10}  {:<20}  {:<20}  {:<25}  {:<25}  {:<20}  {:<21}'.format(*linha))

print('')
print(150*'-')
print('')
print('{:^141}'.format('METODO DA POSICAO FALSA'))
print('')
print('{:<10}  {:<20}  {:<20}  {:<25}  {:<25}  {:<20}  {:<21}'.format(*x))
print('{0:<10}  {0:<20}  {0:<20}  {0:<25}  {0:<25}  {0:<20}  {0:<21}'.format(*sep))
a = antigo_valor[0]
b = antigo_valor[1]
anterior = 0
cont = 1
while True:
    linha = []
    linha.append(cont)
    linha.append(a)
    linha.append(b)
    funcao_a = f(a)
    funcao_b = f(b)
    r_aprox = ((a*funcao_b)-(b*funcao_a))/(funcao_b-funcao_a)
    funcao_x = f(r_aprox)
    linha.append(funcao_a)
    linha.append(funcao_b)
    linha.append(r_aprox)
    linha.append(funcao_x)
    if anterior == r_aprox:
        for i in range(30):
            print('{:<10}  {:<20}  {:<20}  {:<25}  {:<25}  {:<20}  {:<21}'.format(*linha))
            cont += 1
            linha[0] = cont
        break
    if funcao_x*funcao_a > 0:
        a = r_aprox
    else:
        b = r_aprox
    anterior = r_aprox
    cont += 1
    print('{:<10}  {:<20}  {:<20}  {:<25}  {:<25}  {:<20}  {:<21}'.format(*linha))

x = ['Iteracao', 'x', 'f(x)']
print('')
print(150*'-')
print('')
print('{:^141}'.format('METODO DE NEWTON-RAPHSON'))
print('')
print('{:<10}  {:<65}  {:<65}'.format(*x))
print('{0:<10}  {0:<65}  {0:<65}'.format(*sep))

r_aprox = antigo_valor[2]
anterior = 0
cont = 1
while True:
    linha = []
    linha.append(cont)
    linha.append(r_aprox)
    funcao_x = f(r_aprox)
    linha.append(funcao_x)
    if anterior == r_aprox:
        for i in range(30):
            print('{:<10}  {:<65}  {:<65}'.format(*linha))
            cont += 1
            linha[0] = cont
        break
    anterior = r_aprox
    r_aprox = anterior - (f(anterior)/df(anterior))
    cont += 1
    if cont == 30:
        break
    print('{:<10}  {:<65}  {:<65}'.format(*linha))
#print(r_aprox)