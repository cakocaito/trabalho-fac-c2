arquivo = open('nums', 'r')
numBin = arquivo.readline().strip('\n')
numBin1 = arquivo.readline().strip('\n')
arquivo.close()
# numBin = input()
# numBin1 = input()
valorDec = 0
potencia = 31
listaNums = []
for i in numBin:
    numInt = int(i)
    listaNums.append(numInt)
if listaNums[0] == 1:
    listaNums[0] = 0
    for j in range(32):
        valorDec = valorDec + (listaNums[j] * (2 ** potencia))
        potencia = potencia - 1
    valorDec *= -1
elif listaNums[0] == 0:
    for j in range(32):
        valorDec = valorDec + (listaNums[j] * (2 ** potencia))
        potencia = potencia - 1
print(valorDec)
valorDec1 = 0
potencia = 31
listaNums1 = []
for i in numBin1:
    numInt1 = int(i)
    listaNums1.append(numInt1)
if listaNums1[0] == 1:
    listaNums1[0] = 0
    for j in range(32):
        soma1 = valorDec1 + (listaNums1[j] * (2 ** potencia))
        potencia = potencia - 1
    valorDec1 *= -1
elif listaNums1[0] == 0:
    for j in range(32):
        valorDec1 = valorDec1 + (listaNums1[j] * (2 ** potencia))
        potencia = potencia - 1
print(valorDec1)

sobra = 0
soma = 0
subtracao = 0
listaNumsSomadosRev = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
listaNumsRev = list(reversed(listaNums))
listaNums1Rev = list(reversed(listaNums1))
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
listaNumsSomados = list(reversed(listaNumsSomadosRev))
print(listaNumsSomados)