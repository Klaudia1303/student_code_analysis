def A_Ex4(filename,anno):
    a=open(filename)
    b=a.readlines()
    x=0
    c=b[0].strip().split(",")
    for n in range(1,len(c)):
        if int(c[n])==anno:
            x=n
            break
    y=0
    z=""
    for m in range(1,len(b)):
        d=b[m].strip().split(",")
        if int(d[x])>y or (int(d[x])==y and d[0]>z):
            z=d[0]
            y=int(d[x])
    a.close()
    return z
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""
     
###############################################################################

"""TEST FUNZIONE, NON MODIFICARE"""

if __name__ == '__main__':
    from tester import tester_fun

    counter_test_positivi = 0
    total_tests = 5

    counter_test_positivi += tester_fun(A_Ex4, ['Vendite1.csv',2012] , 'Giubbotto')
    counter_test_positivi += tester_fun(A_Ex4, ['Vendite2.csv',2012] , 'Maglione')
    counter_test_positivi += tester_fun(A_Ex4, ['Vendite2.csv',2013] , 'Zaino')
    counter_test_positivi += tester_fun(A_Ex4, ['Vendite3.csv',2011] , 'Giubbotto')
    counter_test_positivi += tester_fun(A_Ex4, ['Vendite3.csv',2010] , 'Cellulare')
    
    print('La funzione',A_Ex4.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
