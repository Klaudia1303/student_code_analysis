def A_Ex3(fileName):
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""
    #Scrivere una funzione che prende ingresso una stringa fileName, nome di un file csv,
    #contenente le informazioni sugli esami superati dagli studenti (nel formato
    #Matricola,Voto,Materia), e restituisce un dizionario con chiave il nome dell’esame e valore la lista
    #ordinata delle matricole (rappresentate come interi) che hanno superato quell’esame, cioè hanno preso
    #almeno 18. 

    f=open(fileName,"r",encoding="UTF-8")
    t=f.readline()
    d={}
    lettura=f.readlines()
    for elem in lettura:
        elem=elem.strip().split(",")
        #print(elem)
        if int(elem[1])>=18:
            if elem[2] not in d:
                d[elem[2]]=[int(elem[0])]
            else:
                d[elem[2]]+=[int(elem[0])]
                d[elem[2]].sort()
    return d


        


###############################################################################

"""NON MODIFICARE, codice di testing della funzione"""

if __name__ == '__main__':
    from tester import tester_fun

    counter_test_positivi = 0
    total_tests = 5

    counter_test_positivi += tester_fun(A_Ex3, ["esami1.csv"] , {'Fisica': [1345, 1753], 'Analisi': [1346], 'Geometria': [1896]})
    counter_test_positivi += tester_fun(A_Ex3, ["esami2.csv"] , {'Analisi': [1346]})
    counter_test_positivi += tester_fun(A_Ex3, ["esami3.csv"] , {'Analisi': [1347, 1348], 'Ricerca Operativa': [1347, 1349]})
    counter_test_positivi += tester_fun(A_Ex3, ["esami4.csv"] , {'Basi di Dati': [1012, 1100], 'Analisi': [1021]})
    counter_test_positivi += tester_fun(A_Ex3, ["esami5.csv"] , {'Fisica': [1345], 'Fondamenti': [1987], 'Analisi': [1346], 'Geometria': [1896]})

    print('La funzione',A_Ex3.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
