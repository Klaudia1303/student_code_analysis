def A_Ex5(filename,oggetto):
    f = open(filename, encoding = "UTF-8")
    a = f.readline()
    listaAnni = a.strip().split(",")
    crescita = 0
    indiceAnno = 0
    for i in f.readlines():
        riga = i.strip().split(",")
        if oggetto in riga:
            for j in range(1, len(riga) -1):
                diff = int(riga[j + 1]) - int(riga[j])
                if diff >= crescita:
                    crescita = diff
                    indiceAnno = j + 1
            
    if crescita == 0:
        indiceAnno = 1
    return int(listaAnni[indiceAnno])
                    
                
                

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
