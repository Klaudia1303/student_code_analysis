def A_Ex5(filename,oggetto):
    f=open(filename,encoding='UTF-8')
    r0=f.readline().strip().split(',')
    a=0
    ind=0
    for riga in f:
        r=riga.strip().split(',')
        if r[0]==oggetto:
            for i in r[1:]:
                for j in r[1:]:
                    b=int(j)-int(i)
                    if int(b)>int(a):
                        a=b
                        ind=int(r.index(j))
            if a==0:
                ind=0
            s=int(r0[ind])
    return s
            
    
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
