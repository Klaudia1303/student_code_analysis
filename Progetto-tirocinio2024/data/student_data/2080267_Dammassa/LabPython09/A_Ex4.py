def A_Ex4(filename,anno):
    f = open(filename, encoding= "UTF-8")
    mass = ""
    n = 0
    for riga in f:
        riga = riga.split(",")
        if(riga[0] == "Anno"):
            for i in range(len(riga)):
                if(riga[i] != "Anno" and int(riga[i]) == anno):
                    pos = i
        if riga[0] != "Anno" and int(riga[pos]) > n:
            mass = riga[0]
            n = int(riga[pos])
            if riga != "Anno" and int(riga[pos]) == n:
                if riga[pos] > mass:
                    mass = riga[pos]
                    n = int(riga[pos])
    f.close()
    return mass
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
