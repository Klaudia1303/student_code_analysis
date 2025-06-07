def A_Ex3(fileName):
    f=open(fileName,'r',encoding="UTF-8")
    u=f.readlines()
    d={}
    for riga in u:
        l=[]
        x=riga.strip().split(',')
        if x[0]=='Matricola':
            continue
        a=int(x[0])
        b=int(x[1])
        c=x[2]
        k=d.keys()
        if b>17 and (c not in k):
            l.append(a)
            l.sort()
            d[c]=l
        elif b>17 and (c in k):
            q=d[c]
            q.append(a)
            q.sort()
            d[c]=q
    f.close()
    return d


    
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""

###############################################################################

"""NON MODIFICARE, codice di testing della funzione"""

if __name__ == '__main__':
    from tester import tester_fun

    counter_test_positivi = 0
    total_tests = 5

    counter_test_positivi += tester_fun(A_Ex3, ["esami1.csv"] , {'Fisica': [1345, 1753], 'Analisi': [1346], 'Geometria': [1896]})
    counter_test_positivi += tester_fun(A_Ex3, ["esami2.csv"] , {'Analisi': [1346]})
    counter_test_positivi += tester_fun(A_Ex3, ["esami3.csv"] , {'Analisi': [1347, 1348], 'Ricerca Operativa': [1347, 1349]})
    counter_test_positivi += tester_fun(A_Ex3, ["esami4.csv"] , {'Basi di Dati': [1012, 1100], 'Analisi': [1021]})
    counter_test_positivi += tester_fun(A_Ex3, ["esami5.csv"] , {'Fisica': [1345], 'Fondamenti': [1987], 'Analisi': [1346], 'Geometria': [1896]})

    print('La funzione',A_Ex3.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
