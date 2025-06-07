def A_Ex4(filename,anno):
    f = open(filename, encoding = "UTF-8")
    a = f.readline()
    b = a.strip().split(",")
    c = 0
    for i in range(len(b)):
        if str(anno) == b[i]:
            c = i
            break
    vendite = 0
    oggetto = ""
    for riga in f.readlines():
        lista = riga.strip().split(",")
        if int(lista[i]) > vendite:
            vendite = int(lista[i])
            oggetto = lista[0]
        elif int(lista[i]) == vendite:
            if lista[0] > oggetto:
                vendite = int(lista[i])
                oggetto = lista[0]
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
