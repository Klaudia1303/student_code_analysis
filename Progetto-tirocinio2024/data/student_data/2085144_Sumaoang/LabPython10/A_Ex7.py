    
primo = -1
pareggio  = 0
secondo = 1

def A_Ex7(file):
    f = open(file, encoding="UTF-8")
    f.readline()

    d = {}

    for x in f:
        a1 = x.strip()
        a2 = a1.split(",")
        r = risultato(a2)
        b(d, a2, r)

    return d

def punteggio(i, k):
    if k in i:
        return i[k]
    return 0

def b(i, a2, r):
    prima_squadra = a2[0]
    seconda_squadra = a2[1]

    if not prima_squadra in i:
        i[prima_squadra] = 0
    if not seconda_squadra in i:
        i[seconda_squadra] = 0

    if r == pareggio:
        i[prima_squadra] += 1
        i[seconda_squadra] += 1
    elif r == primo:
        i[prima_squadra] += 3
    else:
        i[seconda_squadra] += 3

def risultato(a2):
    punteggio_primo = int(a2[2])
    punteggio_secondo = int(a2[3])
    if  punteggio_primo == punteggio_secondo :
        return pareggio
    elif  punteggio_primo > punteggio_secondo:
        return primo
    else:
        return secondo


 
###############################################################################

"""NON MODIFICARE, codice di testing della funzione"""

if __name__ == '__main__':
    from tester import tester_fun

    counter_test_positivi = 0
    total_tests = 5

    counter_test_positivi += tester_fun(A_Ex7, ["partite1.csv"] , {'Chelsea': 3, 'Everton': 3, 'Arsenal': 4, 'Tottenham': 1})
    counter_test_positivi += tester_fun(A_Ex7, ["partite2.csv"] , {'Chelsea': 4, 'Everton': 6, 'Arsenal': 4, 'Tottenham': 2})
    counter_test_positivi += tester_fun(A_Ex7, ["partite3.csv"] , {'Bayern': 4, 'Schalke': 3, 'Amburgo': 4, 'Werder': 1, 'Colonia': 4, 'Stoccarda': 0})
    counter_test_positivi += tester_fun(A_Ex7, ["partite4.csv"] , {'Bayern': 8, 'Schalke': 6, 'Amburgo': 8, 'Werder': 2, 'Colonia': 8, 'Stoccarda': 0})
    counter_test_positivi += tester_fun(A_Ex7, ["partite5.csv"] , {'Bayern': 5, 'Schalke': 6, 'Amburgo': 5, 'Werder': 5, 'Colonia': 5, 'Stoccarda': 6})

    print('La funzione',A_Ex7.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
