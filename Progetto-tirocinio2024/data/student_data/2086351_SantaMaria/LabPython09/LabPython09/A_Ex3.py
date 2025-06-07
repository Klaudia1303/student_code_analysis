def A_Ex3(fileName):
    fin=open(fileName,'r',encoding='UTF-8')
    s=fin.readline()
    ris=set()
    for riga in fin:
        l=riga.split(',')
        voto=int(l[1])
        materia=l[2].replace('\n','')
        if voto>=29:
            s=open(fileName,'r',encoding='UTF-8')
            b=s.readline()
            for riga1 in s:
                l1=riga1.split(',')
                if int(l1[1])>=29 and materia==l1[2].replace('\n','') and l[0]!=l1[0]:
                    ris.add(materia)
    return ris
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
