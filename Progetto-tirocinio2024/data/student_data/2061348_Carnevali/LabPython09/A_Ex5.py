def A_Ex5(filename,oggetto):
    a=open(filename)
    b=a.readlines()
    for n in range(1,len(b)):
        c=b[n].split(",")
        if c[0]==oggetto:
            x=0
            y=1
            for m in range(2,len(c)):
                if int(c[m])-int(c[m-1])>x or (int(c[m])-int(c[m-1])==x and b[0].split(",")[m]>b[0].split(",")[y]):
                    x=int(c[m])-int(c[m-1])
                    y=m
    a.close()
    return int(b[0].strip().split(",")[y])
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
