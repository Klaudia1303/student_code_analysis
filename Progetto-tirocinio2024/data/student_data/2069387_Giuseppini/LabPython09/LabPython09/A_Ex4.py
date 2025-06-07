def A_Ex4(filename,anno):
    f=open(filename,encoding='utf-8')
    s=f.readline()
    s1=f.read()
    c=0
    ogg=''
    riga1=s.strip().split(',')
    l=s1.split('\n')
    if str(anno) in riga1 :
        i=riga1.index(str(anno))
        for righe in l:
            ll=righe.strip().split(',')
            if int(ll[i])>c:
                c=int(ll[i])
                vinc=ll[0]
    return vinc
    
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
