def A_Ex4(filename,anno):
    s=open(filename, encoding='UTF-8')
    r=s.readline().strip().split(',')
    dmax='.'
    max=0
    for a in range(1,len(r)):
        if int(r[a])==int(anno):
            break
    s.close
    l=[]
    s=open(filename, encoding='UTF-8').readlines()
    for elem in s[1:]:
        r=elem.strip().split(',')
        l.append((r[0],r[a]))
    for i in l:
        if int(i[1])>max:
            max=int(i[1])
            dmax=i[0]
        elif int(i[1])==max and i[0]>dmax:
            max=int(i[1])
            dmax=i[0]
    return dmax
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
