primaSquadra= -1
pareggio = 0
secondaSquadra = 1

def A_Ex9(fileName,squadra):

    f = open(fileName, encoding="UTF-8")
    f.readline()

    b = {}

    for l in f:
        r1 = l.strip()
        r2 = r1.split(",")
        risultato = risultato_partita(r2)
        b1(b , r2 , risultato)

    return punteggio(b, squadra)

def punteggio(b, key):
    if key in b:
        return b[key]
    return 0

def b1(b, r2, risultato):
    prima_squadra = r2[0]
    seconda_squadra = r2[1]
    
    if not prima_squadra in b:
        b[prima_squadra] = 0
    if not seconda_squadra in b:
        b[seconda_squadra] = 0

    if risultato == pareggio:
        b[prima_squadra] += 1
        b[seconda_squadra] += 1
    elif risultato == primaSquadra:
        b[prima_squadra] += 3
    else:
        b[seconda_squadra] += 3

def risultato_partita(r2):
    punteggio_prima_squadra = r2[2]
    punteggio_seconda_squadra = r2[3]
    if punteggio_prima_squadra == punteggio_seconda_squadra:
        return pareggio
    elif punteggio_prima_squadra > punteggio_seconda_squadra:
        return primaSquadra
    else:
        return secondaSquadra
 
###############################################################################

"""TEST FUNZIONE, NON MODIFICARE"""

if __name__ == '__main__':
    from tester import tester_fun

    counter_test_positivi = 0
    total_tests = 5

    counter_test_positivi += tester_fun(A_Ex9, ["partite1.csv",'Chelsea'] , 3)
    counter_test_positivi += tester_fun(A_Ex9, ["partite1.csv",'Tottenham'] , 1)
    counter_test_positivi += tester_fun(A_Ex9, ["partite2.csv",'Arsenal'] , 4)
    counter_test_positivi += tester_fun(A_Ex9, ["partite2.csv",'Bayern'] , 0)
    counter_test_positivi += tester_fun(A_Ex9, ["partite3.csv",'Bayern'] , 4)

    print('La funzione',A_Ex9.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
