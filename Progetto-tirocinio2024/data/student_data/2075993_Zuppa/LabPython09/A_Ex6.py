def A_Ex6(filename):
    fin=open(filename,encoding='UTF-8')
    anni=fin.readline().strip().split(',')
    l=[]
    for i in fin:
        l.append(i.strip().split(','))
    fin.close()
    M=0
    for i in range(1,len(anni)):
        s=0
        for j in range(0,len(l)):
            s+=int(l[j][i])
        if s>=M:
            M=s
            a=anni[i]
    return int(a)
            
 
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
