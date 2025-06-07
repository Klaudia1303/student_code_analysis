#Scrivere una funzione che prende in ingresso due insiemi a e b di coppie (cioè tuple di dimensione due) tali che
#l'insieme a contiene le coppie (nome, cittanascita) (ogni coppia indica che quella persona è nata in quella città)
#e l'insieme b contiene le coppie (citta, regione) (ogni coppia indica
#che quella città appartiene a quella regione). La funzione deve restituire un altro insieme contenente
#tutte e sole le coppie (nome, regione) che indicano che quella persona è nata in quella regione.
#Ad esempio, se a={('Giovanni', 'Napoli'), ('Marco', 'Roma'), ('Giuseppe', 'Rieti'), ('Aldo', 'Torino')}
#e b={('Napoli', 'Campania'), ('Benevento', 'Campania'), ('Roma', 'Lazio'), ('Rieti', 'Lazio'), ('Genova', 'Liguria')},
#allora l'insieme da restituire sarà {('Giovanni', 'Campania'), ('Marco', 'Lazio'), ('Giuseppe', 'Lazio')}.
#Si assuma che a e b siano insiemi che contengono solo coppie i cui elementi sono stringhe, oppure che siano vuoti.
#Se una città è presente in a ma non in b allora la persona nata in quella città NON deve essere nell’insieme risultato.
#Ovviamente, se uno dei due insiemi in ingresso è vuoto, la funzione deve restituire un insieme vuoto.

def A_Ex5(a,b):
    c=set()
    if a==set() or b==set():
        return c
    a=list(a)
    b=list(b)
    for i in a:
        for j in b:
            if i[1]==j[0]:
                c.add((i[0],j[1]))
    return c

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
