def A_Ex4(fileName):
    file=open(fileName,'r',encoding='UTF-8')
    file.readline()
    i=set()
    l=[]
    d={}
    for line in file:
        line=line.strip().split(',')
        l.append(line)
        i.add(int(line[0]))
    file.close()
    for e in i:
        d[e]=0
    for el in l:
        if int(el[1])>17:
            d[int(el[0])]+=1
    datogliere=[]
    for key in d:
        if d[key]==0:
            datogliere.append(key)
    for e in datogliere:
        d.pop(e)
    return d
        
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""

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
