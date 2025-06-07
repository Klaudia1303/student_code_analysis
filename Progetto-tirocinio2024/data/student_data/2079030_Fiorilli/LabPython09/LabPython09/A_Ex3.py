def A_Ex3(fileName):
    file=open(fileName, encoding="UTF-8")
    riga=file.readline()
    riga=riga.strip().split(',')
    A=set()
    L=[]
    c=0
    for i in riga:
        if i=='Materia':
            mat=c
        elif i=='Voto':
            voto=c
        c+=1
    riga=file.readline()
    while len(riga)>0:
        riga=riga.strip().split(',')
        if int(riga[voto])>=29:
            L.append(riga[mat])
        riga=file.readline()
    file.close()
    for i in L:
        if L.count(i)>=2:
            A.add(i)
    return A

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
