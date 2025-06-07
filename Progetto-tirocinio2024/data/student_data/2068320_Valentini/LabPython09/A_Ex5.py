def A_Ex5(filename,oggetto):
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""
    f = open(filename)
    r = f.readlines()
    for i in range(1, len(r)):
        singole_vendite = r[i].split(",")
        if singole_vendite[0] != oggetto:
            continue
        else:

            indice = 1
            crescita = 1
            for k in range(1, len(singole_vendite)-1):
                if int(singole_vendite[k]) < int(singole_vendite[k+1]) and (int(singole_vendite[k+1])-int(singole_vendite[k]))>=crescita:
                    crescita = int(singole_vendite[k+1])-int(singole_vendite[k])
                    indice = k+1
            anni = r[0].split(",")
            anno = anni[indice]
    return(int(anno))
                    
                
            
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
