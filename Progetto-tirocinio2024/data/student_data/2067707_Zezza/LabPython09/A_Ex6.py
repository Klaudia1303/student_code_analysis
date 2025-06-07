def A_Ex6(filename):
    valori=[]
    SOM=0    
    ContaOggetti=0
    f=open(filename,encoding='UTF-8')
    riga1=f.readline().strip().split(',')
    for riga in f:
        riga=riga.strip().split(',')
        ContaAnni=len(riga)-1
        ContaOggetti+=1
        for val in riga:
            if val.isdecimal()==True:
                valori.append(val)
    anno=0
    for i in range(ContaOggetti+1):
        ValoriAnno=valori[i::ContaAnni]
        som=0
        anno+=1
        for j in ValoriAnno:
            som+=int(j)
        if som>=SOM:
            SOM=som
            ANNO=riga1[anno]
    f.close()
    return int(ANNO)
            
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
