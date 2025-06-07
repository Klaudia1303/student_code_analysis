def A_Ex5(filename,oggetto):
    c=open(filename, encoding='UTF-8')
    F=c.readline()
    v=F.strip().split(',')
    a=[]
    for i in range(1,len(v)):
        a.append(v[i])
    for i in c:
        r= i.strip().split(',')
        if r[0]==oggetto:
            d=0
            a1=1
            for j in range (2,len(r)):
                if int(r[j])-int(r[j-1])>=d:
                    d=int(r[j])-int(r[j-1])
                    a1=j
    c.close
                
                
    return int(a[a1-1])
    
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
