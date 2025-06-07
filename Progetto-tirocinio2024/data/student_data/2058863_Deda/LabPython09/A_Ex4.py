def A_Ex4(filename,anno):
    f=open(filename,'r',encoding="UTF-8")
    s=f.readlines()
    a=-1
    w=s[0].strip().split(',')
    for i in range(1,len(s)):
        q=s[i].strip().split(',')
        for j in range(1,len(w)):
            if int(w[j])==anno and int(q[j])>a:
                a=int(q[j])
                k=q[0]
                print(a,k)
            if int(w[j])==anno and int(q[j])==a:
                if q[0]>k:
                    a=int(q[j])
                    k=q[0]
    f.close()
    return k
        
    
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
