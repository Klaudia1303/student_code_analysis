def A_Ex3(fileName):
    f=open(fileName,'r',encoding="UTF-8")
    materie=[]
    lfile=[]
    lfin=[]
    for el in f:
        l=el.split(',')
        l[2]=l[2].strip()
        materie.append(l[2])
        lfile.append(l)
    for i in range(len(materie)):
        if materie.count(materie[i])>=2:
            if not lfile[i][1].isalpha():
                if int(lfile[i][1])>=29:
                    lfin.append(materie[i])
    insieme=set(lfin)
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
