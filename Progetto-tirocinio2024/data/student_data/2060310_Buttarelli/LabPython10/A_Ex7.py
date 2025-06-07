def A_Ex7(file):
    d = {}
    l = []
    f = open(file, encoding = "UTF-8")
    contatore = 0
    for i in f:
        i = i.strip().split(",")
        l.append(i)
    for i in range(1, len(l)):
        for j in range(2):
            if l[i][j] not in d:
                if l[i][j] == l[i][0]:
                    if int(l[i][2]) > int(l[i][3]):
                        contatore += 3
                    elif int(l[i][2]) == int(l[i][3]):
                        contatore += 1
                elif l[i][j] == l[i][1]:
                    if int(l[i][3]) > int(l[i][2]):
                        contatore += 3
                    elif int(l[i][3]) == int(l[i][2]):
                        contatore += 1
                d[l[i][j]] = contatore
                contatore = 0
            else:
                contatore = d.get(l[i][j])
                if l[i][j] == l[i][0]:
                    if int(l[i][2]) > int(l[i][3]):
                        contatore += 3
                    elif int(l[i][2]) == int(l[i][3]):
                        contatore += 1
                elif l[i][j] == l[i][1]:
                    if int(l[i][3]) > int(l[i][2]):
                        contatore += 3
                    elif int(l[i][3]) == int(l[i][2]):
                        contatore += 1
                d[l[i][j]] = contatore
                contatore = 0
    f.close()
    return d
 
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
