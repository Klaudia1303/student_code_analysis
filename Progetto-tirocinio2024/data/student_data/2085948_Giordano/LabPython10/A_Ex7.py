def A_Ex7(file):
    f = open(file,encoding="UTF-8")
    f.readline()
    d = {}
    for i in f:
        x = "".join(i.strip().split("\n"))
        xs = x.strip().split(',')
        if xs[0] not in d:
            d[xs[0]] = 0
        if xs[1] not in d:
            d[xs[1]] = 0
    f.close()
    f = open(file,encoding="UTF-8")
    f.readline()
    for i in f:
        x = "".join(i.strip().split("\n"))
        xs = x.strip().split(',')
        if int(xs[2]) > int(xs[3]):
            d[xs[0]] += 3
        elif int(xs[2]) < int(xs[3]):
            d[xs[1]] += 3
        else:
            d[xs[0]] += 1
            d[xs[1]] += 1
    f.close()
    return d

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
