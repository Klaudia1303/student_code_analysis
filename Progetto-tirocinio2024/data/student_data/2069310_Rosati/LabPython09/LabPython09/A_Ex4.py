def A_Ex4(filename,anno):
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""
    s=open(filename, encoding='UTF-8')
    t=s.readline().strip().split(',')
    cmax='.'
    max=0
    for a in range(1,len(t)):
        if int(t[a])==int(anno):
            break
    s.close
    l=[]
    s=open(filename, encoding='UTF-8').readlines()
    for elem in s[1:]:
        t=elem.strip().split(',')
        l.append((t[0],t[a]))
    for i in l:
        if int(i[1])>max:
            max=int(i[1])
            cmax=i[0]
        elif int(i[1])==max and i[0]>cmax:
            max=int(i[1])
            cmax=i[0]
    return cmax
        
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
