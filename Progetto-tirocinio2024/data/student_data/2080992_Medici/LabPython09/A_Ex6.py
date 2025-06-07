def A_Ex6(filename):
    f=open(filename, encoding="UTF-8")
    d={}
    massimo=0
    anno=0
    riga1=f.readline().strip().split(",")
    for riga in f:
        riga=riga.strip().split(",");
        for i in range(1,len(riga1)):
            d[int(riga1[i])]=0
            for j in range(1,len(riga)):
                if i==j:
                    d[int(riga1[i])]+=int(riga[j])
                    break
            if massimo<d[int(riga1[i])]:
                anno=riga1[j]
                massimo=d[int(riga1[i])]
            elif massimo==d[int(riga1[i])]:
                anno=max(anno,riga1[j])
    f.close()
    return int(anno)
        
        
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
