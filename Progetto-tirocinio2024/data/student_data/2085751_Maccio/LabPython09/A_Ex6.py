def A_Ex6(filename):
    file=open(filename,'r',encoding='UTF-8')
    a=file.readline().strip().split(',')
    v=0
    s=file.readline().strip().split('\n')
    for i in a:
        if i=='Anno':
            continue
        indice=a.index(i)
        ve=0
        for j in s:
            j=j.strip().split(',')
            ve+=int(j[indice])
        if ve>v:
            v=ve
            anno=int(i)
        elif ve==v:
            anno=max(anno,int(i))
    file.close()
    return anno
    
    

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
