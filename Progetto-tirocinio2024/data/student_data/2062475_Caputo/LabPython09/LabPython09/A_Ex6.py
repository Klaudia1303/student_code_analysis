def A_Ex6(filename):
    f = open (filename, "r", encoding = "UTF-8")
    rigaAnno = f.readline()
    rigaAnno = rigaAnno.strip().split(",")
    f.close()
    massimo = 0
    anno = 0

    for i in range (1, len(rigaAnno)):
        f = open (filename, "r", encoding = "UTF-8")
        rigaAnno = f.readline()
        rigaAnno = rigaAnno.strip().split(",")
        somma = 0
        for riga in f:
            riga = riga.strip().split(",")
            somma = somma + int(riga[i])
        f.close()
        if somma > massimo:
            massimo = somma
            anno = rigaAnno[i]
        elif somma == massimo and int(rigaAnno[i]) > int(anno):
            massimo = somma
            anno = rigaAnno[i]
    anno = int(anno)
    return anno
            
        
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
