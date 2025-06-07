def A_Ex4(fileName):
    f=open(fileName,encoding='UTF-8')
    sv=[]
    d={}
    esami=0
    for elem in f:
        elem=elem.strip().split(',')
        sv.append(elem)
        

    for i in range(1,len(sv)):
        voto=int(sv[i][1])
        if voto>=18:
            matricola=int(sv[i][0])
            d[matricola]=d.get(matricola,0)+1
        
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
