def A_Ex5(filename,oggetto):
    f = open(filename, "r")

    riga = f.readline()
    anni = riga.strip().split(",")

    lista = []
    anno = 0

    while len(riga) > 0:
        riga = f.readline()
        lista = riga.strip().split(",")
        if lista[0] == oggetto:
            precedente = 0
            ass = 0
            for x in range(1,len(lista)):
                if x == 1: 
                    anno = anni[x]
                if ass <= (int(lista[x]) - precedente) and x > 1:
                    ass = int(lista[x]) - precedente
                    anno = anni[x]
                precedente = int(lista[x])
            break

    f.close()

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
