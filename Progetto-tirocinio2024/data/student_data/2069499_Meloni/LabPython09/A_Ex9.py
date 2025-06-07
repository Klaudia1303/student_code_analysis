def A_Ex9(fileName,squadra):
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""
    fin=open(fileName,encoding="UTF-8")
    fin.readline()
    s_tot=[]
    for elem in fin:
        elem=elem.strip().split(',')
        s_tot.append(elem)

    fin.close()
    count=0
    
    indice=[]
    for i in range(len(s_tot)):
        for j in range(len(s_tot[i])):
            if squadra == s_tot[i][j]:
                indice.append((i,j))

    for k in range (len(indice)):
        if indice[k][1]==1:
            if s_tot[(indice[k][0])][3]>s_tot[(indice[k][0])][2]:
                count+=3
            if s_tot[(indice[k][0])][3]==s_tot[(indice[k][0])][2]:
                count+=1
        if indice[k][1]==0:
            if s_tot[(indice[k][0])][2]>s_tot[(indice[k][0])][3]:
                count+=3
            if s_tot[(indice[k][0])][2]==s_tot[(indice[k][0])][3]:
                count+=1
    
    return(count)
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
