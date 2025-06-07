def A_Ex4(filename,anno):
    f=open(filename,encoding='UTF-8')
    fr=f.readlines()
    year=str(anno)
    maxx=0
    ob=''
    n=fr[0].strip().split(',').index(year)
    for pos in range(1,len(fr)):
        fr[pos]=fr[pos].strip().split(',')
        if int(fr[pos][n])>maxx:
            maxx=int(fr[pos][n])
            ob=fr[pos][0]
        elif int(fr[pos][n])==maxx:
            ob=max(fr[pos][0])
    f.close()
    return ob
            
        
    
    
        
     
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
