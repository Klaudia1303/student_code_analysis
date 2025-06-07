def A_Ex5(a,b):
    if not a or not b:
        return set()

    r_set = set()
    for nome, a_citta in a:
        # se la citta di a non è presente tra le citta di b, itera al prossimo elemento
        if a_citta not in [b_citta for b_citta,_ in b]:
            continue
        
        for b_citta, regione in b:
            # se le citta delle due tuple non corrispondono, itera al prossimo
            if a_citta != b_citta:
                continue
            r_set.add((nome, regione))

    return r_set

###############################################################################

"""NON MODIFICARE IL SEGUENTE CODICE (codice di test della funzione)"""

if __name__ == '__main__':
    from tester import tester_fun

    """SE NON VOLETE ESEGUIRE UN TEST COMMENTATE LA RIGA RELATIVA CON #"""
    counter_test_positivi = 0
    total_tests = 5

    counter_test_positivi += tester_fun(A_Ex5, [{('Giovanni', 'Napoli'), ('Marco', 'Roma'), ('Giuseppe', 'Rieti'), ('Aldo', 'Torino')}, {('Napoli', 'Campania'), ('Benevento', 'Campania'), ('Roma', 'Lazio'), ('Rieti', 'Lazio'), ('Genova', 'Liguria')}] , {('Giovanni', 'Campania'), ('Marco', 'Lazio'), ('Giuseppe', 'Lazio')})
    counter_test_positivi += tester_fun(A_Ex5, [{('Giovanni', 'Napoli')}, {('Roma', 'Lazio')}] , set())
    counter_test_positivi += tester_fun(A_Ex5, [set(), {('Napoli', 'Campania')}] , set())
    counter_test_positivi += tester_fun(A_Ex5, [{('Giovanni', 'Napoli'), }, {('Napoli', 'Campania')}] , {('Giovanni', 'Campania')})
    counter_test_positivi += tester_fun(A_Ex5, [{('Giovanni', 'Napoli'), ('Marco', 'Roma')}, {('Napoli', 'Campania'), ('Roma', 'Lazio'), ('Rieti', 'Lazio')}] , {('Giovanni', 'Campania'), ('Marco', 'Lazio')})

    print('La funzione',A_Ex5.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
