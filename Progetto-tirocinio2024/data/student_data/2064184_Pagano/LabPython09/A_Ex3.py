def A_Ex3(fileName): # matricola, voto, materia
    f = open(fileName, encoding="UTF-8")
    dataset = [row.strip().split(",") for row in f.readlines()]
    dataset.pop(0)
    
    result = set()
    subjects = set()
    
    # primo ciclo per ottenere la lista delle materie
    for data in dataset:
        subjects.add(data[2])

    # ciclo per ogni materia che controlla tutti gli studenti
    for subject in subjects:
        validStudents = 0
        for data in dataset:
            if data[2] == subject and int(data[1]) >= 29:
                validStudents += 1
                if validStudents >= 2:
                    break
        
        if validStudents >= 2:
            result.add(subject)

    return result
        

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
