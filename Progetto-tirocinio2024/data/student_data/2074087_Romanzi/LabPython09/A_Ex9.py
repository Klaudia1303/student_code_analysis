def A_Ex9(fileName,squadra):

    f=open(fileName, encoding="UTF-8")
    ls=[]
    lt=[]
    y=0
    for i in f:
        i=i.strip().split(",")
        ls.append(i)
    for j in range(1,len(ls)):
        for z in range(0,2):
            if [ls[j][z], 0] not in lt:
                lt.append([ls[j][z], 0])
    for c in range(1,len(ls)):
        if int(ls[c][2])==int(ls[c][3]):
            for p in range(len(lt)):
                if lt[p][0]==ls[c][0]:
                    lt[p][1]=int(lt[p][1])+1
            for o in range(len(lt)):
                if lt[o][0]==ls[c][1]:
                    lt[o][1]=int(lt[o][1])+1
        if int(ls[c][2])>int(ls[c][3]):
            for q in range(len(lt)):
                if lt[q][0]==ls[c][0]:
                    lt[q][1]=int(lt[q][1])+3
        if int(ls[c][2])<int(ls[c][3]):
            for w in range(len(lt)):
                if lt[w][0]==ls[c][1]:
                    lt[w][1]=int(lt[w][1])+3
    for u in range(len(lt)):
        if lt[u][0]==squadra:
            y=int(lt[u][1])
    f.close()
    return y
    
    
 
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
