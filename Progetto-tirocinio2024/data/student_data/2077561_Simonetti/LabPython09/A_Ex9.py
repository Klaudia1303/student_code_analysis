def A_Ex9(fileName,squadra):
    fin=open(fileName,encoding='UTF-8')
    next(fin)
    fullList=[]
    points=0
    for line in fin:
        line=line.strip().split(',')
        fullList.append(line)
    relevantLists=[]
    for j in fullList:
        if squadra in j:
            relevantLists.append(j)
    for i in relevantLists:
        if i.index(squadra)==0:
            if i[2]>i[3]:
                points+=3
            if i[2]==i[3]:
                points+=1
        elif i.index(squadra)==1:
            if i[2]==i[3]:
                points+=1
            if i[2]<i[3]:
                points+=3
              
    return points
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
