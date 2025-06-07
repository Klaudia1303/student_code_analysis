def A_Ex6(filename):
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""
    f = open(filename,"r",encoding="UTF-8")
    anni = f.readline().strip().split(",")
    somma = 0
    anno = anni[1]

    for i in range(1,len(anni)):
        somma_temp =0
        for riga in f:
            lista = riga.strip().split(",")
            somma_temp += int(lista[i])
        if somma_temp > somma:
            somma = somma_temp
            anno = anni[i]
        f.close()
        f = open(filename,"r",encoding="UTF-8")
        f.readline()
    return int(anno)
            
    
 
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
