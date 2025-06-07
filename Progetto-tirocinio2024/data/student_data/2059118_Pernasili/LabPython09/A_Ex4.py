def A_Ex4(filename,anno):
    f = open(filename,encoding="UTF-8")
    s = f.read()
    f.close
    l = []
    m = 0
    ss = ''
    k = 0
    a = s.split('\n')
    print(anno)
    for i in range(len(a)):
        r = []
        aa = a[i].replace('\n',',')
        r = aa.split(',')
        if i == 0:
            print(r)
            for j in range(1,len(r[i])):
                if r[j] == str(anno):
                    print('test2')
                    k = j
                    print(j,anno)
        else:
            l.append((r[0],r[k]))
    for k in range(len(l)):
         if l[k][1]>str(m):
             m= l[k][1]
             ss= l[k][0]
    return ss
                
    
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
