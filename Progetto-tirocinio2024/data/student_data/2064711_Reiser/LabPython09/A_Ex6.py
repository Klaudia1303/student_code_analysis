def A_Ex6(filename):
    f=open(filename,encoding="UTF-8")
    l1=[]
    for riga in f:
        riga=riga.strip().split(",")
        l1.append(riga)
    mass=0
    anno=0
    a=1
    b=0
    riga1=l1[0]
    for i in range(1,len(riga1)):
        for j in l1[1:]:
            mass+=int(j[i])
            if mass>=anno:
                anno=mass
                b=i
        mass=0
    mass=0
    return int(riga1[b])
    f.close()
    
 
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
