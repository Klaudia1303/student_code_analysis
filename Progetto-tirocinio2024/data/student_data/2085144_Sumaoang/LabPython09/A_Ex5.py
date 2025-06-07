def A_Ex5(filename,oggetto):
    f = open(filename, encoding = "UTF-8" )
    i1 = f.readline()
    i2 = i1.strip()
    i3 = i2.split(",")

    j = None
    for x in f:
        j1 = x.strip()
        j2 = j1.split(",")
        if j2[0] == oggetto:
            j = j2

    if j is None:
        return

    vendita = -1
    i_vendita = -1

    for a in range(1, len(j)):
        if int(j[a]) > vendita:
            vendita = int(j[a])
            i_vendita = a
            
    return int(i3[i_vendita])

    
    
    

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
