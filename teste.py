arquivo = open('nums', 'r')
numBin = arquivo.readline().strip('\n')
numBin1 = arquivo.readline().strip('\n')
arquivo.close()
# numBin = input()
# numBin1 = input()
valorDec = 0
potencia = 31
listaNums = []
listaNumsConv = []
listaNumsConv1 = []
for i in numBin:
    numInt = int(i)
    listaNums.append(numInt)
for k in listaNums:
    listaNumsConv.append(k)
if listaNumsConv[0] == 1:
    listaNumsConv[0] = 0
    for j in range(32):
        valorDec = valorDec + (listaNumsConv[j] * (2 ** potencia))
        potencia = potencia - 1
    valorDec *= -1
elif listaNumsConv[0] == 0:
    for j in range(32):
        valorDec = valorDec + (listaNumsConv[j] * (2 ** potencia))
        potencia = potencia - 1
print(valorDec)
valorDec1 = 0
potencia = 31
listaNums1 = []
for i in numBin1:
    numInt1 = int(i)
    listaNums1.append(numInt1)
for k in listaNums1:
    listaNumsConv1.append(k)
if listaNumsConv1[0] == 1:
    listaNumsConv1[0] = 0
    for j in range(32):
        soma1 = valorDec1 + (listaNumsConv1[j] * (2 ** potencia))
        potencia = potencia - 1
    valorDec1 *= -1
elif listaNumsConv1[0] == 0:
    for j in range(32):
        valorDec1 = valorDec1 + (listaNumsConv1[j] * (2 ** potencia))
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
somaConv = 0
potencia = 31
if listaNumsSomados[0] == 1:
    listaNumsSomados[0] = 0
    for j in range(32):
        somaConv = somaConv + (listaNumsSomados[j] * (2 ** potencia))
        potencia = potencia - 1
    somaConv *= -1
elif listaNumsSomados[0] == 0:
    for j in range(32):
        somaConv = somaConv + (listaNumsSomados[j] * (2 ** potencia))
        potencia = potencia - 1

listaNumsSubtraidosRev = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
for i in range(len(listaNumsSomadosRev)):
    if listaNumsRev[i] == 0 and listaNums1Rev[i] == 0:
        listaNumsSubtraidosRev[i] = 0
    elif listaNumsRev[i] == 1 and listaNums1Rev[i] == 1:
        listaNumsSubtraidosRev[i] = 0
    elif listaNumsRev[i] == 0 and listaNums1Rev[i] == 1:
        listaNumsSubtraidosRev[i] = 1
    elif listaNumsRev[i] == 1 and listaNums1Rev[i] == 0:
        listaNumsSubtraidosRev[i] = 1
listaNumsSubtraidos = list(reversed(listaNumsSubtraidosRev))
print(listaNumsSubtraidos)
subtConv = 0
potencia = 31
if listaNumsSubtraidos[0] == 1:
    listaNumsSubtraidos[0] = 0
    for j in range(32):
        subtConv = subtConv + (listaNumsSubtraidos[j] * (2 ** potencia))
        potencia = potencia - 1
    subtConv *= -1
elif listaNumsSubtraidos[0] == 0:
    for j in range(32):
        subtConv = subtConv + (listaNumsSubtraidos[j] * (2 ** potencia))
        potencia = potencia - 1
print(somaConv)
print(subtConv)