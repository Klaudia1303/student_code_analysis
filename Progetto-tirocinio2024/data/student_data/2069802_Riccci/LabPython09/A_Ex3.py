def A_Ex3(fileName):
    f = open(fileName, encoding="UTF-8")
    f.readline()
    check = []
    cont = 0
    materie = []
    file = []
    for riga in f:
        file.append(riga.replace('\n',''))
    f.close()
    file2 = file.copy()
    for el in file:
        cont = 0
        materia = el.split(',')[2]
        if(materia not in check):
            for riga2 in file2:
                voto = int(riga2.split(',')[1])
                if(materia in riga2 and voto >= 29):
                    cont += 1
            if(cont == 2): materie.append(materia)
        check.append(el.split(',')[2])
    return set(materie)

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
