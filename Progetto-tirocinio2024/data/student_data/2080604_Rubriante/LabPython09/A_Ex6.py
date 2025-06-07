def A_Ex6(filename):
    f=open(filename,encoding="UTF-8")
    for i in f:
        i=i.strip().split(",")
        l=[0 for j in range(len(i)-1)]
        break
    f.close()
    f=open(filename,encoding="UTF-8")
    con=0
    mas=0
    for i in f:
        i=i.strip().split(",")
        if i[0]=="Anno":
            continue
        else:
            for elem in range(len(i)):
                if i[elem].isalpha()==False:
                    con=int(l[elem-1])
                    con=con+int(i[elem])
                    l[elem-1]=con
    mas=l.index(max(l))
    f.close()
    f=open(filename,encoding="UTF-8")
    for i in f:
        i=i.strip().split(",")
        anno=int(i[mas+1])
        break
    f.close()
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
