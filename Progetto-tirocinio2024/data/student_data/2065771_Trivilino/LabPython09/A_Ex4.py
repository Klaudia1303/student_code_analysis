def A_Ex4(filename,anno):
    f=open(filename,encoding="UTF-8")
    vendite=0
    anni=f.readline().strip().split(",")
    for i in range(1,len(anni)):
        if anno==int(anni[i]):
            indice=i
            break
            
    for elem in f:
        dati=elem.strip().split(",")
        if int(dati[indice])>vendite:
            vendite=int(dati[indice])
            oggetto=dati[0]

        
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
