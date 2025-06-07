def A_Ex4(filename,anno):
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""
    f=open(filename,encoding="UTF-8")
    vendite=0
    oggetto=''
    riga=f.readline()
    anni=riga.strip().split(',')
    for i in range(len(anni)):
        if anni[i].isdecimal() and int(anni[i])==anno:
            an=i
    for elem in f:
        elem=elem.strip().split(',')
        if int(elem[an])>=vendite:
            vendite=int(elem[an])
            oggetto=str(elem[0])
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
