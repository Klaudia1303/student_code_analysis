def A_Ex5(filename,oggetto):
    f= open(filename,encoding='UTF-8')
    s=f.readline()
    p=s.strip().split(',')
    a=[]
    for c in range(1,len(p)):
        a.append(p[c])
    for c in f:
        k=c.strip().split(',')
        if k[0]==oggetto:
            d=0
            a1=1
            for i in range(2,len(k)):
                if int(k[i])-int(k[i-1])>=d:
                    d=int(k[i])-int(k[i-1])
                    a1=i
    f.close()
    ris= int(a[a1-1])
    return ris




    
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
