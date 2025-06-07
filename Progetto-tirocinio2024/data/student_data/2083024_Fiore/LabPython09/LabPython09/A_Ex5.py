def A_Ex5(filename,oggetto):
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""
    f = open(filename, "r", encoding= "UTF-8")
    lista_anni = f.readline().strip().split(",")
    crescita = 0
    anno = lista_anni[1]
    
    for riga in f:
        lista = riga.strip().split(",")
        if lista[0] == oggetto:
            for i in range(2, len(lista)):
                if int(lista[i])-int(lista[i-1]) >= crescita:
                    crescita = int(lista[i])-int(lista[i-1])
                    anno = lista_anni[i]
    return int(anno)
                
    
    

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
