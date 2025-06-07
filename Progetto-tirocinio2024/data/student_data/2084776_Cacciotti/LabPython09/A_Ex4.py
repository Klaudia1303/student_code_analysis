def A_Ex4(filename,anno):
    f=open(filename, encoding='UTF-8')
    f1=f.readline()
    f1=f1.strip().split(',')
    ind=0
    cont=0
    prod=''
    for i in range(1, len(f1)):
        if(anno == int(f1[i])):
            ind=i
    f1=f.readlines()
    for i in range(len(f1)):
        f2=f1[i].strip().split(',')
        if(int(f2[ind])>cont):
            prod=f2[0]
            cont=int(f2[ind])
    f.close()
    return prod
        
    
    
     
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
