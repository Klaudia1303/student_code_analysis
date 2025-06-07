def A_Ex3(fileName):
    f=open(fileName,encoding="UTF-8")
    riga=f.readline()
    s=f.read()
    l=s.strip().split("\n")
    l1=[]
    for elem in l:
        elem1=elem.split(",")
        l1.append(elem1)
    l2=[]
    for elem in l1:
        if int(elem[1])>=29:
            l2.append(elem[2])
    risi=[]
    for elem in l2:
        if l2.count(elem)>=2 and elem not in risi:
            risi.append(elem)
    ris=set(risi)
    f.close()
    return ris


###############################################################################

"""NON MODIFICARE, codice di testing della funzione"""

if __name__ == '__main__':
    from tester import tester_fun
    
    counter_test_positivi = 0
    total_tests = 5

    counter_test_positivi += tester_fun(A_Ex3, ["esami1.csv"], {'Fisica'})
    counter_test_positivi += tester_fun(A_Ex3, ["esami2.csv"], set())
    counter_test_positivi += tester_fun(A_Ex3, ["esami3.csv"], {'Ricerca Operativa','Analisi'})
    counter_test_positivi += tester_fun(A_Ex3, ["esami4.csv"], {'Basi di Dati'})
    counter_test_positivi += tester_fun(A_Ex3, ["esami5.csv"], set())

    print('La funzione',A_Ex3.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
