def A_Ex6(filename):
    f=open(filename,encoding="UTF-8")
    s=f.read()
    sclear=s.replace("\n",";")
    l=s.strip().split("\n")
    l1=[]
    for elem in l:
        elem1=elem.split(";")
        l1.append(elem1)
    l2=[]
    for elem in l1:
        elem2=elem[0].split(",")
        l2.append(elem2)
    vndmax=0
    anno=0
    for i in range(1,len(l2[0])):
        vndann=0
        for n in range(1,len(l2)):
            vndann+=int(l2[n][i])
        if vndann>=vndmax:
            vndmax=vndann
            anno=int(l2[0][i])
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
