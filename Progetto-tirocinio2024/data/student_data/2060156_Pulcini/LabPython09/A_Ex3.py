def A_Ex3(fileName):
    f = open(fileName,'r',encoding='UTF-8')
    lista1=[]
    lista2=[]
    insieme=set()
    primariga=f.readline()
    for riga in f:
        riga=riga.strip().split(',')
        if int(riga[1])>=29:
            lista1.append(riga[2])
    for elem in lista1:
        if lista1.count(elem)>=2:
            lista2.append(elem)
    for materia in lista2:
        if materia not in insieme:
            insieme.add(materia)
    f.close()
    return insieme
    
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""

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
