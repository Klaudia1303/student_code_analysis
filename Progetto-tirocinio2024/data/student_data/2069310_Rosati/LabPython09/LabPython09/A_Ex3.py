def A_Ex3(fileName):
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""
    insieme=set()
    s=open(fileName, encoding='UTF-8').readlines()
    for riga in s[1:]:
        l=[]
        t=riga.strip().split(',')
        for i in s[1:]:
            f=i.strip().split(',')
            if f[2]==t[2]:
                l.append(f[1])

        c=0
        for v in l:
            if int(v)>=29:
                c+=1
                if c>=2:
                    insieme.add(t[2])
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
