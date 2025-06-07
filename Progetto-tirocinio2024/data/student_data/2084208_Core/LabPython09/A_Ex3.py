def A_Ex3(fileName):
    insieme=set()
    f=open(fileName)
    riga=f.readline()
    elementi=riga.strip().split(',')
    riga=f.readline()
    dati=riga.strip().split(',')
    l=[]
    while len(riga)>0:
        if int(dati[1])>=29:
            l.append((dati[1],dati[2]))
        riga=f.readline()
        dati=riga.strip().split(',')
    for i in range (len(l)-1):
            tupla=l[i]
            tupla1=l[i+1]
            if tupla[1] in tupla1[1] and tupla[1] not in insieme:
                insieme.add(tupla[1])
            else:
                numero=0
                for j in range(len(l)):
                    if tupla[1] in l[j]:
                        numero+=1
                if numero>=2:
                    insieme.add(tupla[1])
    f.close()
    return insieme

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
