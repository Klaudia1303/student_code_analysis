def A_Ex4(filename,anno):
    #"""MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""
    f=open(filename,encoding='UTF-8')
    s=f.readline()
    s=s.strip().split(',')
    s=list(s)
    pos=s.index(str(anno))
    l=[]
    for riga in f:
        riga=riga.strip().split(',')
        t=(riga[0],riga[pos])
        l.append(t)
    f.close()
    s=''
    Max=0
    for vendite in l:
        if int(vendite[1])>Max:
            s=vendite[0]
            Max=int(vendite[1])
        if int(vendite[1])==Max:
            k=[]
            k.append(s)
            k.append(vendite[0])
            k.sort()
            s=k[0]
    return s
    
     
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
