def A_Ex4(filename,anno):
    file = open(filename,'r',encoding='UTF-8')
    M = 0

    anni = file.readline()
    anni = anni.strip().split(',') #lista di anni
    #print(anni)

    indice_anno = anni.index(str(anno))
    indice_anno = int(indice_anno) #indice colonna
    
    #print('colonna: ',indice_anno)

     

    for riga in file:
        #isolo in lista l'oggetto e i numeri di vedita 
        riga = riga.strip().split(',')

        
        vendite = int(riga[indice_anno])
        if vendite > M:
            M = vendite
            oggetto = riga[0]
            #print(oggetto,vendite,M)

        elif vendite == M and riga[0] > oggetto:
            oggetto = riga[0]
            #print(oggetto,M)
    file.close()
    
    return oggetto
            
            
        
    
     





















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
