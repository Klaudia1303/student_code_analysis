def A_Ex4(fileName):
    f=open(fileName, encoding="UTF-8")
    s=f.readline()
    S=f.read()
    l=S.strip().split("\n")
    d={}
    l1=[]
    for elem in l:
        elem1=elem.strip().split(",")
        l1.append(elem1)
    for elem in l1:
        if int(elem[1])>17:
            if int(elem[0]) not in d:
                d[int(elem[0])]=1
            else:
                d[int(elem[0])]+=1
    f.close()
    return d

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
