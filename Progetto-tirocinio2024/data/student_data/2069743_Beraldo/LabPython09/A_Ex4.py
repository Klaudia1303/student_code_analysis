def A_Ex4(filename,anno):
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""
    file = open(filename,'r',encoding='UTF-8')

    anni = file.readline().strip().split(',')
   
    pos = anni.index(str(anno))
    maxVen = 0
    prodotto = ''
    for riga in file:
        vendite = riga.strip().split(',')
        if( int(vendite[pos]) > maxVen):
            prodotto = vendite[0]
            maxVen = int(vendite[pos])
        elif(int(vendite[pos]) == maxVen):
            print(vendite[0] + prodotto) 
            if(ord(prodotto) < ord(vendite[0])):
               prodotto = vendite[0]
               maxVen = int(vendite[pos])
    return prodotto
      
         
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
