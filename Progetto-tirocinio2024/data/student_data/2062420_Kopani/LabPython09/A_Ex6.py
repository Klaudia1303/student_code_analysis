def A_Ex6(filename):
    f=open(filename,encoding="UTF-8")
    l=f.readlines()
    L=[]
    for i in range(len(l)):
        s=l[i]
        ls=s.strip().split(',')
        L.append(ls)
    f.close()
    k=1
    sommaMax=0
    indice=0
    while k<len(L[0]):
        somma=0
        for j in range(1,len(L)):
            riga=L[j]
            somma=somma+int(riga[k])
        if somma>=sommaMax:
            sommaMax=somma
            indice=k
        k+=1
    anno=int(L[0][indice])
    return anno	
 		
 
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
