def A_Ex4(filename,anno):
    s= open(filename,encoding="UTF-8")
    l=[]
    for r in s :
        l.append(r.strip().split(','))
    s.close()
    a=0
    o=0
    f=''
    for c in range(len(l[0])):
        if l[0][c]==str(anno):
            a=c
            break
    l.remove(l[0])
    for i in l:
        if int(i[a])>o or (int(i[a])==o and i[0]>f):
            o=int(i[a])
            f=i[0]
    return f

    


    
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
