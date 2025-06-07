def A_Ex6(filename):
    f = open(filename, encoding = "UTF-8")
    a = f.readline()
    listaAnni = a.strip().split(",")
    l = ["somme"]
    for numeri in range(len(listaAnni)):
        l.append(0)
    for i in f.readlines():
        riga = i.strip().split(",")
        for j in range(1, len(riga)):
            l[j] = l[j] + int(riga[j])
    num = 0
    indiceAnno = 0
    for k in range(1, len(l)):
        if l[k] >= num:
            num = l[k]
            indiceAnno = k
    return int(listaAnni[indiceAnno])
        
 
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
