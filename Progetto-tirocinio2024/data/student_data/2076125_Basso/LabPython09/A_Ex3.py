def A_Ex3(fileName):
    f=open(fileName)
    l=[]
    i=set()
    riga=f.readline()
    riga=f.readline()
    dati=riga.strip().split(',')
    while len(riga)>0:
        if int(dati[1])>=29:
            l.append(dati[2])
        riga=f.readline()
        dati=riga.strip().split(',')
    for m in l:
        if l.count(m)>=2:
            i.add(m)
    f.close()
    return i
    
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
