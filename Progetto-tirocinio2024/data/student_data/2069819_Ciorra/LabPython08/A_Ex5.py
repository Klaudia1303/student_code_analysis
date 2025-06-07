from tester import tester_fun

def A_Ex5(a,b):
    r=set()
    for t in a:
        for tu in b:
            if t[1]==tu[0]:
                r.add((t[0],tu[1]))
    return r

###############################################################################

"""NON MODIFICARE IL SEGUENTE CODICE (codice di test della funzione)"""

if __name__ == '__main__':
    from tester import tester_fun

    """SE NON VOLETE ESEGUIRE UN TEST COMMENTATE LA RIGA RELATIVA CON #"""
    counter_test_positivi = 0
    total_tests = 10

    counter_test_positivi += tester_fun(A_Ex5, [{('Giovanni', 'Napoli'), ('Marco', 'Roma'), ('Giuseppe', 'Rieti'), ('Aldo', 'Torino')}, {('Napoli', 'Campania'), ('Benevento', 'Campania'), ('Roma', 'Lazio'), ('Rieti', 'Lazio'), ('Genova', 'Liguria')}] , {('Giovanni', 'Campania'), ('Marco', 'Lazio'), ('Giuseppe', 'Lazio')})
    counter_test_positivi += tester_fun(A_Ex5, [{('Giovanni', 'Napoli')}, {('Roma', 'Lazio')}] , set())
    counter_test_positivi += tester_fun(A_Ex5, [set(), {('Napoli', 'Campania')}] , set())
    counter_test_positivi += tester_fun(A_Ex5, [{('Giovanni', 'Napoli'), }, {('Napoli', 'Campania')}] , {('Giovanni', 'Campania')})
    counter_test_positivi += tester_fun(A_Ex5, [{('Giovanni', 'Napoli'), ('Marco', 'Roma')}, {('Napoli', 'Campania'), ('Roma', 'Lazio'), ('Rieti', 'Lazio')}] , {('Giovanni', 'Campania'), ('Marco', 'Lazio')})

    counter_test_positivi += tester_fun(A_Ex5, [set(), set()] , set())
    counter_test_positivi += tester_fun(A_Ex5, [{('Anastasio', 'Minervino'), ('Luca','Popoli')}, \
        {('Milano', 'Lombardia'), ('Popoli', 'Abruzzo'), ('Minervino','Puglia')}], \
            {('Anastasio', 'Puglia'), ('Luca', 'Abruzzo')})
    counter_test_positivi += tester_fun(A_Ex5, [{('Anastasio', 'Minervino')}, \
        {('Milano', 'Lombardia')}], \
            set())
    counter_test_positivi += tester_fun(A_Ex5, [{('Anastasio', 'Minervino')}, \
        {('Minervino','Puglia')}], \
            {('Anastasio', 'Puglia')})
    counter_test_positivi += tester_fun(A_Ex5, [{('Anastasio', 'Minervino'), ('Alice', 'Minervino'), ('Luca', 'Minervino')}, \
        {('Minervino','Puglia'), ('Milano', 'Lombardia')}], \
            {('Anastasio', 'Puglia'), ('Alice', 'Puglia'), ('Luca', 'Puglia')})
    


    print('La funzione',A_Ex5.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
