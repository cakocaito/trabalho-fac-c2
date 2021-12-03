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


def c2(listaParaC2):
    listaSoma1 = [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    listaSomada1 = []
    for i in range(len(listaParaC2)):
        if listaParaC2[i] == 0:
            listaSomada1.append(1)
        else:
            listaSomada1.append(0)
    listaParaSomar1 = list(reversed(listaSomada1))
    listaSoma1Fim = soma(listaParaSomar1, listaSoma1)
    listaFim = converte(listaSoma1Fim)
    listaFim *= -1
    return listaFim



#Leitura arquivo com os dois binários em string
arquivo = open('entrada.txt', 'r')
numBin = arquivo.readline().strip('\n')
numBin1 = arquivo.readline().strip('\n')
arquivo.close()

#Listas utilizadas
listaNums = []
listaNumsConv = []
listaNumsConv1 = []
listaNums1 = []
listaC2 = []
lista1C2 = []
listaNumsC2 = []
listaNums1C2 = []
listaC2Soma = []
listaC2Subt = []
listaNumsC2Soma = []
listaNumsC2Subt = []

#Transformação dos números binários em inteiro e adicionando às listas
for i in numBin:
    numInt = int(i)
    listaNums.append(numInt)
    listaNumsConv.append(numInt)
    listaNumsC2.append(numInt)
    listaNumsC2Soma.append(numInt)
for i in numBin1:
    numInt1 = int(i)
    listaNums1.append(numInt1)
    listaNumsConv1.append(numInt1)
    listaNums1C2.append(numInt1)
    listaNumsC2Subt.append(numInt1)

#Lista invertida para realizar a soma/subtração
listaContrario = list(reversed(listaNums))
listaContrario1 = list(reversed(listaNums1))

#Conversão base 2 para base 10, usando sinal e magnitude
conversaoNum = converte(listaNumsConv)
conversaoNum1 = converte(listaNumsConv1)
print(conversaoNum)
print(conversaoNum1)
espaco()

#Soma e subtração dos números na base 2
listaNumsSomados = soma(listaContrario, listaContrario1)
listaNumsSubtraidos = subtracao(listaContrario, listaContrario1)
print(*listaNumsSubtraidos, sep = "")
print(*listaNumsSomados, sep = "")
espaco()

#Conversão do resultado da soma e subtração
conversaoSoma = converte(listaNumsSomados)
conversaoSubt = converte(listaNumsSubtraidos)
print(conversaoSubt)
print(conversaoSoma)
espaco()

#Conversão dos números usando complemento de 2
if listaNumsC2[0] == 0:
    listaC2 = converte(listaNumsC2)
else:
    listaC2 = c2(listaNumsC2)
if listaNums1C2[0] == 0:
    lista1C2 = converte(listaNums1C2)
else:
    lista1C2 = c2(listaNums1C2)
print(listaC2)
print(lista1C2)
espaco()

listaSomaParaC2 = soma(listaContrario, listaContrario1)
ListaSubtParaC2 = subtracao(listaContrario, listaContrario1)
print(*listaSomaParaC2, sep = "")
print(*ListaSubtParaC2, sep = "")
espaco()

#Conversão da some e subtração dos números na base 2 usando complemento de 2
if listaSomaParaC2[0] == 0:
    listaC2Soma = converte(listaSomaParaC2)
else:
    listaC2Soma = c2(listaSomaParaC2)
if ListaSubtParaC2[0] == 0:
    listaC2Subt = converte(ListaSubtParaC2)
else:
    listaC2Subt= c2(ListaSubtParaC2)
print(listaC2Soma)
print(listaC2Subt)




