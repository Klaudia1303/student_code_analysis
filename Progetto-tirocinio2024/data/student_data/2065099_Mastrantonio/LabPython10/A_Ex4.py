def A_Ex4(fileName):
    file = open(fileName , encoding = 'UTF-8')
    l = []
    for elem in file:
        elem = elem.strip().split(',')
        l.append(elem)
    d = {}
    print(l)
    for i in range(1,len(l)):
        riga = l[i]
        matricola = int(riga[0])
        if matricola not in d and int(riga[1]) >= 18:
            d [matricola] = 0
            d [matricola] = d[matricola] + 1                
        elif matricola in d:
            if int(riga[1]) >= 18 :
                d [matricola] = d[matricola] + 1
    return(d)
            

    
###############################################################################


"""NON MODIFICARE, codice di testing della funzione"""

if __name__ == '__main__':
    from tester import tester_fun

    counter_test_positivi = 0
    total_tests = 5

    counter_test_positivi += tester_fun(A_Ex4, ["esami1.csv"] , {1345: 1, 1346: 1, 1896: 1, 1753: 1})
    counter_test_positivi += tester_fun(A_Ex4, ["esami2.csv"] , {1346: 1})
    counter_test_positivi += tester_fun(A_Ex4, ["esami3.csv"] , {1347: 2, 1348: 1, 1349: 1})
    counter_test_positivi += tester_fun(A_Ex4, ["esami4.csv"] , {1100: 1, 1012: 1, 1021: 1})
    counter_test_positivi += tester_fun(A_Ex4, ["esami5.csv"] , {1345: 1, 1987: 1, 1346: 1, 1896: 1})

    print('La funzione',A_Ex4.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
