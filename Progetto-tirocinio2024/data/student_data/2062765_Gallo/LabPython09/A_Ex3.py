def A_Ex3(fileName):
    f=open(fileName,"r",encoding="UTF-8")
    s=set()
    riga=f.readline()
    lmaterie=[]
    l=[]
    while len(riga)>0:
        riga=f.readline()
        if len(riga)>0:
            dati=riga.strip().split(",")
            if dati[0] not in l:
                l.append(dati[0])
                if int(dati[1])>=18:
                    if dati[2] in lmaterie:
                        s.add(dati[2])
                    else:
                        lmaterie.append(dati[2])
            else:
                if int(dati[1])>=18:
                    if dati[2] not in lmaterie:
                        s.add(dati[2])
    return s
            

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
