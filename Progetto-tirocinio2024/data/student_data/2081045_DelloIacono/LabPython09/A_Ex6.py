def A_Ex6(filename):
    f = open(filename, encoding = "UTF-8")
    tot = 0
    totale = 0
    pos = 0
    for riga0 in f:
        riga0 = riga0.split(",")
        for i in range(1, len(riga0)):
            f1 = open(filename, encoding = "UTF-8")
            for riga in f1:
                riga = riga.split(",")
                if(riga[0] != "Anno" and riga[i].isalpha() == False):
                    tot = tot + int(riga[i])
            if(tot > totale):
                totale = tot
                pos = i
            tot = 0
        tot = int(riga0[pos].strip())
        break
    f.close()
    f1.close()
    return(tot)
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""
 
###############################################################################

"""NON MODIFICARE, codice di testing della funzione"""

if __name__ == '__main__':
    from tester import tester_fun

    counter_test_positivi = 0
    total_tests = 5

    counter_test_positivi += tester_fun(A_Ex6, ['Vendite1.csv'] , 2010)
    counter_test_positivi += tester_fun(A_Ex6, ['Vendite2.csv'] , 2013)
    counter_test_positivi += tester_fun(A_Ex6, ['Vendite3.csv'] , 2013)
    counter_test_positivi += tester_fun(A_Ex6, ['Vendite4.csv'] , 2020)
    counter_test_positivi += tester_fun(A_Ex6, ['Vendite5.csv'] , 2022)

    print('La funzione',A_Ex6.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
