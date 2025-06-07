def A_Ex9(fileName,squadra):
    f=open(fileName,encoding="UTF-8")
    l=f.readlines()
    L=[]
    for i in range(len(l)):
        s=l[i]
        ls=s.strip().split(',')
        L.append(ls)
    f.close()
    L.remove(L[0])
    punteggio=0
    for j in range(len(L)):
        if squadra not in L[j]:
            continue
        indice=L[j].index(squadra)
        if indice==0:
            if L[j][2]>L[j][3]:
                punteggio+=3
            elif L[j][2]==L[j][3]:
                punteggio+=1
        else:
            if L[j][3]>L[j][2]:
                punteggio+=3
            elif L[j][2]==L[j][3]:
                punteggio+=1
    return punteggio
 
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
