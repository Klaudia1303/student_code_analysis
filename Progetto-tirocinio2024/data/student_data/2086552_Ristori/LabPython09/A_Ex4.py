def A_Ex4(fileName,anno):
    fin=open(fileName,"r",encoding="UTF-8")
    riga=fin.readline()
    dati=riga.strip().split(",")
    indice=dati.index(str(anno))
    riga=fin.readline()
    numVenditeMax=0
    while len(riga)>0:
        dati=riga.strip().split(",")
        numVendite=int(dati[indice])
        if numVendite>numVenditeMax:
            numVenditeMax=numVendite
            nomeOggetto=dati[0]
        if numVendite==numVenditeMax:
            if dati[0]<nomeOggetto:
                numVenditeMax=numVendite
                nomeOggetto=dati[0]
        riga=fin.readline()
    return nomeOggetto
        
            
            
        
        
    
    









    #"""MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""
     
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
