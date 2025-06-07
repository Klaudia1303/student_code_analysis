def A_Ex9(fileName,squadra):
    
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""
    f=open(fileName,encoding="UTF-8")
    r={}
    next(f)
    l=f.read().strip().split("\n")
    for i in range(len(l),-1,-1):
        l.append(str(l[i-1]).strip().split(","))
        l.remove(l[i-1])
        
    for elem in l:
        if elem[2].isdecimal():
            if elem[1]  not in r:
                r[elem[1]]=0
            if elem[0] not in r:
                r[elem[0]]=0
            if squadra not in r:
                r[squadra]=0
    for z in l:
        if z[2]>z[3]:
            r[z[0]]+=3

        if z[2]<z[3]:
            r[z[1]]+=3

        if z[2]==z[3]:
            r[z[0]]+=1
            r[z[1]]+=1

    return r.get(squadra)
           
###############################################################################

"""TEST FUNZIONE, NON MODIFICARE"""

if __name__ == '__main__':
    from tester import tester_fun

    counter_test_positivi = 0
    total_tests = 5

    counter_test_positivi += tester_fun(A_Ex9, ["partite1.csv",'Chelsea'] , 3)
    counter_test_positivi += tester_fun(A_Ex9, ["partite1.csv",'Tottenham'] , 1)
    counter_test_positivi += tester_fun(A_Ex9, ["partite2.csv",'Arsenal'] , 4)
    counter_test_positivi += tester_fun(A_Ex9, ["partite2.csv",'Bayern'] , 0)
    counter_test_positivi += tester_fun(A_Ex9, ["partite3.csv",'Bayern'] , 4)

    print('La funzione',A_Ex9.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
