def A_Ex5(filename,oggetto):
    f = open(filename, encoding = "UTF-8")
    mass = 0
    pos = 1
    for riga in f:
        riga = riga.split(",")
        if(riga[0] == oggetto):
            for i in range(len(riga)):
                if(riga[i] != oggetto and i != len(riga)-1 and int(riga[i]) <= int (riga[i+1])):
                    pos = i+1
    f.close()
    
    f = open(filename, encoding = "UTF-8")
    for riga in f:
        riga = riga.split(",")
        for i in range(len(riga)):
            if(riga[i] != "Anno" and i == pos):
                mass = int(riga[i])
        break
    
    f.close()
    return(mass)
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""

###############################################################################

"""NON MODIFICARE, codice di testing della funzione"""

if __name__ == '__main__':
    from tester import tester_fun

    counter_test_positivi = 0
    total_tests = 5

    counter_test_positivi += tester_fun(A_Ex5, ['Vendite1.csv','Giubbotto'] , 2012)
    counter_test_positivi += tester_fun(A_Ex5, ['Vendite1.csv','Zaino'] , 2010)
    counter_test_positivi += tester_fun(A_Ex5, ['Vendite2.csv','Maglione'] , 2012)
    counter_test_positivi += tester_fun(A_Ex5, ['Vendite2.csv','Zaino'] , 2013)
    counter_test_positivi += tester_fun(A_Ex5, ['Vendite3.csv','Giubbotto'] , 2013)

    print('La funzione',A_Ex5.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
