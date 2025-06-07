def A_Ex4(filename,anno):
    f=open(filename, 'r', encoding='UTF-8')
    riga1=f.readline()
    riga=riga1.strip().split(',')
    posizione=riga.index(str(anno))
    

    massimo=-1
    elemento=''
    for i in f:
        i=i.strip().split(',')
        if int(i[posizione])>massimo:
            massimo=int(i[posizione])
            elemento=i[0]
        elif i[0]>elemento:
            elemento=i[0]
    f.close()
    return elemento

        
        



     
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
