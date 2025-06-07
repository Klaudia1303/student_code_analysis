def A_Ex6(filename):
    f=open(filename,encoding="UTF-8")
    lista=[]
    for riga in f:
        lista.append(riga.replace('\n','').split(','))
    f.close()
    for i in lista:
        i.remove(i[0])
    lista2=[]
    for i in range(0,len(lista[0])):
        somma=0
        for j in range(1,len(lista)):
            somma+=int(lista[j][i])
        lista2.append(somma)
    indice=0
    for i in range(0,len(lista2)-1):
        if lista2[i]<=lista2[i+1]:
            indice=i+1
    return int(lista[0][indice])

 
###############################################################################

"""NON MODIFICARE, codice di testing della funzione"""

if __name__ == '__main__':
    from tester import tester_fun

    counter_test_positivi = 0
    total_tests = 5

    counter_test_positivi += tester_fun(A_Ex6, ['Vendite1.csv'] , 2010)
    counter_test_positivi += tester_fun(A_Ex6, ['Vendite2.csv'] , 2013)
    counter_test_positivi += tester_fun(A_Ex6, ['Vendite3.csv'] , 2013)
    counter_test_positivi += tester_fun(A_Ex6, ['Vendite4.csv'] , 2020)
    counter_test_positivi += tester_fun(A_Ex6, ['Vendite5.csv'] , 2022)

    print('La funzione',A_Ex6.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
