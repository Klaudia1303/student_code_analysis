def A_Ex3(fileName):
    f=open(fileName,encoding="UTF-8")
    consuma=f.readline()
    voti=[]
    materie=[]
    insieme=set()
    for elem in f:
        m=set()
        elem=elem.strip().split(",")
        if int(elem[1])>=29:
            materie.append(elem[2])
    for j in materie:
        if materie.count(j)>1:
            insieme.add(j)

    f.close()
    return insieme

            
    
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
