def A_Ex3(fileName):
    mat=set()
    f=open(fileName,encoding="UTF-8")
    l=[]
    for elem in f:
        elem=elem.strip().split(",")
        l.append(elem)
    for i in range(1,len(l)):
        count=0
        m=l[i][2]
        for elem in l:
            if elem[2]==m and int(elem[1])>=29:
                count+=1
        if count>1:
            mat.add(m)
    return mat
        

###############################################################################

"""NON MODIFICARE, codice di testing della funzione"""

if __name__ == '__main__':
    from tester import tester_fun
    
    counter_test_positivi = 0
    total_tests = 5

    counter_test_positivi += tester_fun(A_Ex3, ["esami1.csv"], {'Fisica'})
    counter_test_positivi += tester_fun(A_Ex3, ["esami2.csv"], set())
    counter_test_positivi += tester_fun(A_Ex3, ["esami3.csv"], {'Ricerca Operativa','Analisi'})
    counter_test_positivi += tester_fun(A_Ex3, ["esami4.csv"], {'Basi di Dati'})
    counter_test_positivi += tester_fun(A_Ex3, ["esami5.csv"], set())

    print('La funzione',A_Ex3.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
