def A_Ex4(filename,anno):
    f=open(filename,encoding='UTF-8')
    r0=f.readline().strip().split(',')
    for e in r0:
        if e=='Anno':
            continue
        if int(e)==anno:
            a=int(r0.index(e))
    print(a)
    n=int('0')
    for riga in f:
        if riga=='':
            break
        riga=riga.strip().split(',')
        lr=[riga[0],riga[int(a)]]
        print(lr)
        if int(lr[1])>=int(n):
            n=lr[1]
            b=lr[0]
    f.close()
    return b
        
    
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
