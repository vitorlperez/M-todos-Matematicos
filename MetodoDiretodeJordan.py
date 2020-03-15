#Dadas as equações:
#3*x + 2*y + 4*z = 1
#x + y + 2*z = 2
#4*x + 3*y - 2*z = 3 
def EscalonaTriangular(listaPivo, lista2):
    for i in range(len(listaPivo)):
        if listaPivo[i] != 0:
            aux = i
            break
    print(listaPivo[aux])
    print(lista2[aux])
    m1 = lista2[aux]/listaPivo[aux]
    print(m1)
    list_aux = []
    for i in range(len(listaPivo)):
        list_aux.append((m1*listaPivo[i])-lista2[i])
    for i in range(len(list_aux)):
        list_aux[i] =int(list_aux[i]*listaPivo[aux])
    return list_aux

def MetodoJordan(A):
    A[1] = EscalonaTriangular(A[0], A[1])
    print(A)
    A[2] = EscalonaTriangular(A[0], A[2])
    print(A)
    A[2] = EscalonaTriangular(A[1], A[2])
    print(A)
    A[1] = EscalonaTriangular(A[2], A[1])
    print(A)
    A[0] = EscalonaTriangular(A[2], A[0])
    print(A)
    A[0] = EscalonaTriangular(A[1], A[0])
    return A
A = [[3, 2, 4, 1],[1, 1, 2, 2],[4, 3, -2, 3]]
print(MetodoJordan(A))
print('X1 =', A[0][3]/A[0][0])
print('X2 =', A[1][3]/A[1][1])
print('X3 =', A[2][3]/A[2][2])