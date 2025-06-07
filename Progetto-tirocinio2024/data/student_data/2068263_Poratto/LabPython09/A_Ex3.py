def A_Ex3(fileName):
    f=open(fileName,encoding='UTF-8')
    f.readline()
    s=f.read()
    righe=s.strip().split('\n')
    l=[]
    for riga in righe:
        r=riga.strip().split(',')
        print(r)
        if int(r[1])<18:
            continue
        for riga1 in righe:
            r1=riga1.strip().split(',')
            if r==r1:
                continue
            if r[2]==r1[2]:
                if int(r1[1])>17:
                    l.append(r[2])
    i=set(l)
    return i
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
