def A_Ex4(filename,anno):
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""
    x=open(filename,encoding='UTF-8')
    a=x.readline()
    a=a.strip()
    a=a.split(',')
    c=0
    for i in range(1,len(a)):
        if int(a[i])==int(anno):
            c=i
    x.close()
    p=str()
    b=0
    f=open(filename,encoding='UTF-8')
    z=f.readlines()
    f.close
    for j in z[1:]:
        j=j.split(',')
        if int(j[c])>b:
            b=int(j[c])
            p=j[0]

    return p

    
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
