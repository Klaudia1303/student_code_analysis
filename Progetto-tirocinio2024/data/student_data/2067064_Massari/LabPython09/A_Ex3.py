def A_Ex3(fileName):
    f=open(fileName,encoding="UTF-8")
    righe=f.readlines()
    righe_strip=[]
    materie=[]
    risultato=set()
    for elem in righe:
        righe_strip.append(elem.strip().split(","))

    for i in range(1,len(righe_strip)):
        riga=righe_strip[i]
        voto=riga[1]
        materia=riga[2]
        if int(voto)>=29:
            materie.append(materia)

    for dato in materie:
        if materie.count(dato)>=2:
            risultato.add(dato)

    f.close()

    
            
    

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
