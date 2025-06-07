def A_Ex4(fileName):
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""
    esami = open(fileName,'r', encoding= 'UTF-8')
    esami.readline()
    dizEsami = {}
    for riga in esami:
        values = riga.strip().split(',')
        file = open(fileName,'r', encoding= 'UTF-8')
        matricola = values[0]
        file.readline()
        if(int(matricola) not in dizEsami):
            for esame in file:
                values = esame.strip().split(',')
             
                if(int(values[1]) >= 18 and values[0] == matricola):
                     if(int(matricola) in dizEsami):
                         dizEsami[int(matricola)] = int(dizEsami[int(matricola)] + 1)
                         
                     else:
                         dizEsami[int(matricola)] = 0
                         dizEsami[int(matricola)] = int(dizEsami[int(matricola)] + 1)
    esami.close()
    
    return dizEsami            
            
###############################################################################


"""NON MODIFICARE, codice di testing della funzione"""

if __name__ == '__main__':
    from tester import tester_fun

    counter_test_positivi = 0
    total_tests = 5

    counter_test_positivi += tester_fun(A_Ex4, ["esami1.csv"] , {1345: 1, 1346: 1, 1896: 1, 1753: 1})
    counter_test_positivi += tester_fun(A_Ex4, ["esami2.csv"] , {1346: 1})
    counter_test_positivi += tester_fun(A_Ex4, ["esami3.csv"] , {1347: 2, 1348: 1, 1349: 1})
    counter_test_positivi += tester_fun(A_Ex4, ["esami4.csv"] , {1100: 1, 1012: 1, 1021: 1})
    counter_test_positivi += tester_fun(A_Ex4, ["esami5.csv"] , {1345: 1, 1987: 1, 1346: 1, 1896: 1})

    print('La funzione',A_Ex4.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
