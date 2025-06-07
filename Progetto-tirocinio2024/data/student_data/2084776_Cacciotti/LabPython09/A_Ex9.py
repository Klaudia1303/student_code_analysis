def A_Ex9(fileName,squadra):
    f=open(fileName, encoding='UTF-8')
    l=f.readlines()
    squads=[]
    for i in range(1, len(l)):
        l1=l[i].strip().split(',')
        if(l1[0] not in squads):
            squads.append(l1[0])
            squads.append(0)
        if(l1[1] not in squads):
            squads.append(l1[1])
            squads.append(0)
    for i in range(1, len(l)):
        l1=l[i].strip().split(',')
        n=0
        if(int(l1[2])>int(l1[3])):
            squads[squads.index(l1[0])+1]+=3
        elif(int(l1[3])>int(l1[2])):
            squads[squads.index(l1[1])+1]+=3
        else:
            squads[squads.index(l1[1])+1]+=1
            squads[squads.index(l1[0])+1]+=1
    f.close()
    if(squadra in squads):
        res=squads[squads.index(squadra)+1]
        return res
    else:
        return 0
 
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
