def A_Ex6(fileName):

    f=open(fileName,encoding="UTF-8")
    ls=[]
    s=0
    p=0
    h=0
    for i in f:
        i=i.strip().split(",")
        ls.append(i)
    for j in range(1,len(ls[0])):
        for z in range(1,len(ls)):
            s=s+int(ls[z][j])
        if s>=p:
            p=s
            h=int(ls[0][j])
        s=0
    f.close()
    return h

    
    
 
###############################################################################

"""NON MODIFICARE, codice di testing della funzione"""

if __name__ == '__main__':
    from tester import tester_fun

    counter_test_positivi = 0
    total_tests = 5

    counter_test_positivi += tester_fun(A_Ex6, ['Vendite1.csv'] , 2010)
    counter_test_positivi += tester_fun(A_Ex6, ['Vendite2.csv'] , 2013)
    counter_test_positivi += tester_fun(A_Ex6, ['Vendite3.csv'] , 2013)
    counter_test_positivi += tester_fun(A_Ex6, ['Vendite4.csv'] , 2020)
    counter_test_positivi += tester_fun(A_Ex6, ['Vendite5.csv'] , 2022)

    print('La funzione',A_Ex6.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
