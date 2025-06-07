def A_Ex4(filename,anno):
    f=open(filename,encoding='UTF-8')
    intestaz=f.readline().strip().split(',')
    anno_colonne=intestaz.index(str(anno))
    vend=0
    maxogg=''
    for i in f.readlines():
        i=i.strip().split(',')
        if int(i[anno_colonne])>vend:
            maxogg=i[0]
            vend=int(i[anno_colonne])
        if int(i[anno_colonne])==maxogg and i[0]<maxogg:
                massogg=i[0]
    return maxogg     
           
           
           
           
   
    
    
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
