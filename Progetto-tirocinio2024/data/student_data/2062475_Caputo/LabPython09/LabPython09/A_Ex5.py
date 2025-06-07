def A_Ex5(filename,oggetto):
    f = open(filename, "r", encoding = "UTF-8")
    rigaAnno = f.readline()
    rigaAnno = rigaAnno.strip().split(",")
    ris = []
    quantita = 0
    massimo = 0
    anno = rigaAnno[1]
    
    for riga in f:
        riga = riga.strip().split(",")
        if riga[0] == oggetto:
            for i in range(2, len(riga)):
                differenza = int(riga[i]) - int(riga[i-1])
                if differenza > massimo:
                    massimo = differenza
                    anno = rigaAnno[i]
                elif differenza == massimo and anno < rigaAnno[i]:
                    anno = rigaAnno[i]
            break
    f.close()
    anno = int(anno)
    return anno
            
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
