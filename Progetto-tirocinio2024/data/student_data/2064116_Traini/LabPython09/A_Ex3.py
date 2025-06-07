def A_Ex3(fileName):
    a=open(fileName,'r',encoding='UTF-8')
    c=a.readline()
    risultato=set()
    for riga in a:
        casa=riga.split(',')
        voto1=int(casa[1])
        materia1=casa[2].replace('\n','')
        if voto1>=29:
            c=open(fileName,'r',encoding='UTF-8')
            b=c.readline()
            for riga2 in c:
                casa2=riga2.split(',')
                if int(casa2[1])>=29 and materia1==casa2[2].replace('\n','') and casa[0]!=casa2[0]:
                    risultato.add(materia1)
    return risultato
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""

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
