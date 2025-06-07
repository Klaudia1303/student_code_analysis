def A_Ex5(a,b):
    la=list(a)
    lb=list(b)
    f=set()
    for i in range(len(la)):
        x=la[i]
        for j in range(len(lb)):
            c=x[1]
            y=lb[j]
            d=y[0]
            if c==d:
                p=x[0], y[1]
                f.add(p)
    return f
    

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
