def A_Ex6(filename):
    fin=open(filename,encoding="UTF-8")
    f=fin.readlines()
    fin.close()
    Venditemax=0
    DatiPrinc=f[0].strip().split(",")
    annomax=int(DatiPrinc[1])
    for i in range(1,len(DatiPrinc)):
        vendite=0
        for j in range(1,len(f)):
            Dati=f[j].strip().split(",")
            vendite+=int(Dati[i])
        if vendite>Venditemax:
            Venditemax=vendite
            annomax=int(DatiPrinc[i])
        elif vendite == Venditemax:
            if int(DatiPrinc[i])>annomax:
                Venditemax=vendite
                annomax=int(DatiPrinc[i])

    return annomax
        
    
            
 
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
