def A_Ex7(file):
    file = open(file, encoding = 'UTF-8')
    l = []
    for elem in file:
        elem = elem.strip().split(',')
        l.append(elem)
    cancella = l[0]
    l.remove(cancella)
    d = {}
    for riga in l:
        for elem in riga[:2]:
            if elem not in d:
                d [elem] = 0
    for riga in l:
        team1 = riga[0]
        team2 = riga[1]
        goal1 = int(riga[2])
        goal2 = int(riga[3])
        if goal1>goal2 :
            d[team1] = d[team1] + 3
        elif goal2> goal1:
            d[team2] = d[team2] + 3
        elif goal1 == goal2 :
            d[team1] = d[team1] + 1
            d[team2] = d[team2] + 1
    return(d)

 
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
