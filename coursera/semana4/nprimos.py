from math import sqrt
numero = int(input("Digite o valor de n: "))
aux = 0
aux1 = 0
if numero > 3:
    print(2,'\n',3)
while numero > 1:
    aux = sqrt(numero)
    aux = int(aux)
    aux1 = 0
    while aux >= 2:
        if numero%aux == 0:
            aux1 += 1
        if aux == 2:
            if aux1 == 0:
                print(numero)
        aux -= 1
    numero -=1