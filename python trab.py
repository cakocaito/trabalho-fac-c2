def espaco():
    return print()
    
def converte(listaConverter):
    potencia = 31
    valorDec = 0
    if listaConverter[0] == 1:
        listaConverter[0] = 0
    
        for j in range(32):
            valorDec = valorDec + (listaConverter[j] * (2 ** potencia))
            potencia = potencia - 1
        valorDec *= -1
    
    elif listaConverter[0] == 0:
        for j in range(32):
            valorDec = valorDec + (listaConverter[j] * (2 ** potencia))
            potencia = potencia - 1
    return valorDec


def soma(listaNumsRev, listaNums1Rev):
    sobra = 0
    listaNumsSomadosRev = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0]
    for i in range(len(listaNumsSomadosRev)):

        if listaNumsRev[i] == 0 and listaNums1Rev[i] == 0:

            if sobra == 0:
                listaNumsSomadosRev[i] = 0
            else:
                listaNumsSomadosRev[i] = 1
                sobra = 0

        elif listaNumsRev[i] == 1 and listaNums1Rev[i] == 1:

            if sobra == 0:
                listaNumsSomadosRev[i] = 0
                sobra = 1
            else:
                listaNumsSomadosRev[i] = 1
                sobra = 1
        elif listaNumsRev[i] == 0 and listaNums1Rev[i] == 1:

            if sobra == 0:
                listaNumsSomadosRev[i] = 1
            else:
                listaNumsSomadosRev[i] = 0
                sobra = 1
        elif listaNumsRev[i] == 1 and listaNums1Rev[i] == 0:

            if sobra == 0:
                listaNumsSomadosRev[i] = 1
            else:
                listaNumsSomadosRev[i] = 0
                sobra = 1
    listaSoma = list(reversed(listaNumsSomadosRev))
    return(listaSoma)



def subtracao(listaNumsRev, listaNums1Rev):
    listaNumsSubtraidosRev = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0, 0]
    for i in range(len(listaNumsSubtraidosRev)):
        if listaNumsRev[i] == 0 and listaNums1Rev[i] == 0:
            listaNumsSubtraidosRev[i] = 0

        elif listaNumsRev[i] == 1 and listaNums1Rev[i] == 1:
            listaNumsSubtraidosRev[i] = 0

        elif listaNumsRev[i] == 0 and listaNums1Rev[i] == 1:
            listaNumsSubtraidosRev[i] = 1

        elif listaNumsRev[i] == 1 and listaNums1Rev[i] == 0:
            listaNumsSubtraidosRev[i] = 1
    listaSubtracao = list(reversed(listaNumsSubtraidosRev))
    return(listaSubtracao)


arquivo = open('entrada.txt', 'r')
numBin = arquivo.readline().strip('\n')
numBin1 = arquivo.readline().strip('\n')
arquivo.close()

listaNums = []
listaNumsConv = []
listaNumsConv1 = []
listaNums1 = []

for i in numBin:
    numInt = int(i)
    listaNums.append(numInt)
    listaNumsConv.append(numInt)

for i in numBin1:
    numInt1 = int(i)
    listaNums1.append(numInt1)
    listaNumsConv1.append(numInt1)

listaContrario = list(reversed(listaNums))
listaContrario1 = list(reversed(listaNums1))

listaNumsSomados = soma(listaContrario, listaContrario1)
listaNumsSubtraidos = subtracao(listaContrario, listaContrario1)
conversaoNum = converte(listaNumsConv)
conversaoNum1 = converte(listaNumsConv1)
conversaoSoma = converte(listaNumsSomados)
conversaoSubt = converte(listaNumsSubtraidos)
print(conversaoNum)
print(conversaoNum1)
espaco()
print(*listaNumsSubtraidos, sep = "")
print(*listaNumsSomados, sep = "")
espaco()
print(conversaoSoma)
print(conversaoSubt)


