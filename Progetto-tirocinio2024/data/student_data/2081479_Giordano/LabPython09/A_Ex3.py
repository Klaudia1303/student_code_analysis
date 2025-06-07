def A_Ex3(fileName):
    finalSet=set()
    more29=[]
    with open(fileName) as file:
        txt=file.read().split('\n')
        for scan in txt:
            current=scan.split(',')
            if current[0]!='':
                if current[1].isalpha()==False:
                    if int(current[1])>=29:
                        more29.append(current)
    print(more29)
    for counter in range(len(more29)):
        for counter2 in range(len(more29)):
            if counter2!=counter:
                if more29[counter][2]==more29[counter2][2]:
                    finalSet.add(more29[counter][2])
            else:
                continue
    return finalSet
##################################

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