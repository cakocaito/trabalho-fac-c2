def espaco():
    return print()
    
def converte(listaNumsConv, listaNumsConv1):
    potencia = 31
    valorDec = 0
    valorDec1 = 0
    
    
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

    potencia = 31
    
    if listaNumsConv1[0] == 1:
    
        listaNumsConv1[0] = 0
        for j in range(32):
            valorDec1 = valorDec1 + (listaNumsConv1[j] * (2 ** potencia))
            potencia = potencia - 1
        valorDec1 *= -1
    
    elif listaNumsConv1[0] == 0:
    
        for j in range(32):
            valorDec1 = valorDec1 + (listaNumsConv1[j] * (2 ** potencia))
            potencia = potencia - 1
        
    print(valorDec1)
    return listaNumsConv1, listaNumsConv


arquivo = open('entrada.txt', 'r')
numBin = arquivo.readline().strip('\n')
numBin1 = arquivo.readline().strip('\n')
arquivo.close()


sobra = 0
soma = 0
subtracao = 0
listaNumsSomadosRev = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
listaNumsSubtraidosRev = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
valorDec = 0
potencia = 31
listaNums = []
listaNumsConv = []
listaNumsConv1 = []
listaNums1 = []
subtConv = 0


for i in numBin:
    numInt = int(i)
    listaNums.append(numInt)
    listaNumsConv.append(numInt)

for i in numBin1:
    numInt1 = int(i)
    listaNums1.append(numInt1)
    listaNumsConv1.append(numInt1)

converte(listaNumsConv, listaNumsConv1)


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
            

for i in range(len(listaNumsSomadosRev)):
    
    if listaNumsRev[i] == 0 and listaNums1Rev[i] == 0:
        listaNumsSubtraidosRev[i] = 0
    
    elif listaNumsRev[i] == 1 and listaNums1Rev[i] == 1:
        listaNumsSubtraidosRev[i] = 0
    
    elif listaNumsRev[i] == 0 and listaNums1Rev[i] == 1:
        listaNumsSubtraidosRev[i] = 1
    
    elif listaNumsRev[i] == 1 and listaNums1Rev[i] == 0:
        listaNumsSubtraidosRev[i] = 1
        
        
listaNumsSomados = list(reversed(listaNumsSomadosRev))        
listaNumsSubtraidos = list(reversed(listaNumsSubtraidosRev))

espaco()
print(*listaNumsSubtraidos, sep = "")
print(*listaNumsSomados, sep = "")
espaco()

converte(listaNumsSubtraidos, listaNumsSomados)

