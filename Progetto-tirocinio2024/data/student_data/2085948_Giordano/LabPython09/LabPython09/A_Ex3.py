def A_Ex3(fileName):
    file=open(fileName,encoding="UTF-8")
    lista=[]
    lista2=[]
    lista3=[]
    
    for i in file:
        i=i.strip().split(",")
        lista.append(i)
    for i in range(1,len(lista)):
        if int(lista[i][1])>=29:
            lista2.append(lista[i][2])
    for i in range(0,len(lista2)):
        if lista2.count(lista2[i][2])>1:
            lista3.append(lista2[i][2])

    return lista3

###############################################################################

"""NON MODIFICARE, codice di testing della funzione"""

if __name__ == '__main__':
    from tester import tester_fun
    
    counter_test_positivi = 0
    total_tests = 5

    counter_test_positivi += tester_fun(A_Ex3, ["esami1.csv"], {'Fisica'})
    counter_test_positivi += tester_fun(A_Ex3, ["esami2.csv"], set())
    counter_test_positivi += tester_fun(A_Ex3, ["esami3.csv"], {'Ricerca Operativa','Analisi'})
    counter_test_positivi += tester_fun(A_Ex3, ["esami4.csv"], {'Basi di Dati'})
    counter_test_positivi += tester_fun(A_Ex3, ["esami5.csv"], set())

    print('La funzione',A_Ex3.__name__,'ha superato',counter_test_positivi,'test su',total_tests)