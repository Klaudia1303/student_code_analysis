def A_Ex5(filename,oggetto):
    f=open(filename,encoding='UTF-8')
    s=f.readline()
    s=s.strip().split(',')
    l=[]
    h=[]
    for riga in f:
        riga=riga.strip().split(',')
        l.append(riga)
    for i in range(len(l)):
        if oggetto in l[i]:
            l[i].remove(oggetto)
            h=l[i]
    k=max(h)
    t=h.index(k)
    g=int(s[t+1])
    return g
"""MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""

###############################################################################

"""NON MODIFICARE, codice di testing della funzione"""

if __name__ == '__main__':
    from tester import tester_fun

    counter_test_positivi = 0
    total_tests = 5

    counter_test_positivi += tester_fun(A_Ex5, ['Vendite1.csv','Giubbotto'] , 2012)
    counter_test_positivi += tester_fun(A_Ex5, ['Vendite1.csv','Zaino'] , 2010)
    counter_test_positivi += tester_fun(A_Ex5, ['Vendite2.csv','Maglione'] , 2012)
    counter_test_positivi += tester_fun(A_Ex5, ['Vendite2.csv','Zaino'] , 2013)
    counter_test_positivi += tester_fun(A_Ex5, ['Vendite3.csv','Giubbotto'] , 2013)

    print('La funzione',A_Ex5.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
