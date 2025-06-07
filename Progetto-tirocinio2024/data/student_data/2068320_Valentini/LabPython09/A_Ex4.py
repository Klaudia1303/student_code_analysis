def A_Ex4(filename,anno):
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""
    f = open(filename)
    r = f.readlines()
    anni = r[0].split(",")
    "Trovare l'indice di riferimento dell'anno"
    for i in range(1, len(anni)):
        if int(anni[i]) == anno:
            indice = i
            break
    print(indice)
    venditamax = 0
    oggetto = ""
    "Calcolare la vendita massima"
    for k in range(1, len(r)):
        vendita = r[k].split(",")         
        if int(vendita[indice]) > int(venditamax):
            venditamax = vendita[indice]
            oggetto = vendita[0]
    
    return(oggetto)
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
