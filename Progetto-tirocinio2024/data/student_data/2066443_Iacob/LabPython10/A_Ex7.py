def A_Ex7(file):
    o = open(file, 'r', encoding='UTF-8')
    o.readline()
    diz = {}
    
    for line in o:
        l = "".join(line.strip().split("\n"))
        s = l.strip().split(',')
        if s[0] not in diz:
            diz[s[0]] = 0
        if s[1] not in diz:
            diz[s[1]] = 0
    o.close()
    
    f = open(file, 'r', encoding="UTF-8")
    f.readline()
    for st in f:
        w = "".join(st.strip().split("\n"))
        t = w.strip().split(',')
        if int(t[2]) > int(t[3]):
            diz[t[0]] += 3
        elif int(t[2]) < int(t[3]):
            diz[t[1]] += 3
        else:
            diz[t[0]] += 1
            diz[t[1]] += 1
    f.close()
    
    return diz
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""

 
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
