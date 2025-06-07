def A_Ex5(l):
    risultato = []
    somma = 0
    if l == []:
        risultato = []
    else:
        for i in l:#itera sulle singole stinghe lista
            stringa = i
            for c in stringa:
                somma += ord(c)#sommi i codici unicod di ciascun carattere

            risultato.append(somma)#aggiungi la somma unicod di ogni stringa
            somma = 0 #riazzera la somma alla fine di ogni parola

    return risultato
                
            
        
    
















###############################################################################

"""NON MODIFICARE, codice di testing della funzione"""

if __name__ == '__main__':
    from tester import tester_fun

    """SE NON VOLETE ESEGUIRE UN TEST COMMENTATE LA RIGA RELATIVA CON #"""

    counter_test_positivi = 0
    total_tests = 5

    counter_test_positivi += tester_fun(A_Ex5, [["ama","ma","amaca"]], [303,206,499])
    counter_test_positivi += tester_fun(A_Ex5, [[]], [])
    counter_test_positivi += tester_fun(A_Ex5, [["c"]], [99])
    counter_test_positivi += tester_fun(A_Ex5, [["ciao",""]], [412,0])
    counter_test_positivi += tester_fun(A_Ex5, [["",""]], [0,0])

    print('La funzione',A_Ex5.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
