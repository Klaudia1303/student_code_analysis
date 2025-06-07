def A_Ex6(filename):
    f=open(filename,'r',encoding="UTF-8")
    lfile=[]
    anno=0
    sommain=0
    for el in f:
        l=el.split(',')
        for c in range(len(l)):
            l[c]=l[c].strip()
        lfile.append(l)
    for i in range(len(lfile)):
        for j in range(1,len(lfile[i])):
            somma=0
            for k in range(1,len(lfile)):
                somma+=int(lfile[k][j])
            if somma>=sommain:
                sommain=somma
                anno=int(lfile[0][j])
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
