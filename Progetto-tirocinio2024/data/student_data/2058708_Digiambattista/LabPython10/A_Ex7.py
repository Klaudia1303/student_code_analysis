def A_Ex7(file):
    f = open(file)
    r = f.readlines()
    dizionario = {}
    for l in range(1, len(r)):
        r[l] = r[l].strip().split(",")
        if r[l][0] not in dizionario:
            dizionario.update({r[l][0]:0})
        if r[l][1] not in dizionario:
            dizionario.update({r[l][1]:0})
        if int(r[l][2]) > int(r[l][3]):
            dizionario[r[l][0]] += 3
        if int(r[l][2]) < int(r[l][3]):
             dizionario[r[l][1]] += 3
        if int(r[l][3]) == int(r[l][2]):
            dizionario[r[l][0]] += 1
            dizionario[r[l][1]] += 1
    return dizionario
 
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
