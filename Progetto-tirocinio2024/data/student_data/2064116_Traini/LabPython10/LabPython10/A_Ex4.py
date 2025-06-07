#A_Ex4(fileName): Scrivere una funzione che prende in ingresso una stringa fileName, nome di un file csv 
#che ha lo stesso formato del file descritto nell’esercizio precedente (A_Ex3), e restituisce il dizionario con 
#chiave la matricola (intero) e valore il numero di esami superati. Se il file contiene i dati di sopra, la funzione 
#deve restituire {1345: 1, 1346: 1, 1896: 1, 1753: 1}.
def A_Ex4(fileName):
    fin=open(fileName,encoding='utf-8')
    frasi=[]
    risultato={}
    for riga in fin:
        frasi.append(riga.strip().split(','))
    if len(frasi)!=0:
        frasi.remove(frasi[0])
    for lista in frasi:
        if int(lista[1])>=18:
            if int(lista[0]) not in risultato:
                risultato[int(lista[0])]=0
            risultato[int(lista[0])]+=1
    return risultato
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""

###############################################################################


"""NON MODIFICARE, codice di testing della funzione"""

if __name__ == '__main__':
    from tester import tester_fun

    counter_test_positivi = 0
    total_tests = 5

    counter_test_positivi += tester_fun(A_Ex4, ["esami1.csv"] , {1345: 1, 1346: 1, 1896: 1, 1753: 1})
    counter_test_positivi += tester_fun(A_Ex4, ["esami2.csv"] , {1346: 1})
    counter_test_positivi += tester_fun(A_Ex4, ["esami3.csv"] , {1347: 2, 1348: 1, 1349: 1})
    counter_test_positivi += tester_fun(A_Ex4, ["esami4.csv"] , {1100: 1, 1012: 1, 1021: 1})
    counter_test_positivi += tester_fun(A_Ex4, ["esami5.csv"] , {1345: 1, 1987: 1, 1346: 1, 1896: 1})

    print('La funzione',A_Ex4.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
