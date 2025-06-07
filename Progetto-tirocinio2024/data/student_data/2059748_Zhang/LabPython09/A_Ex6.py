def A_Ex6(filename):
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""
    x=open(filename,encoding='UTF-8')
    a=x.readline()
    a=a.strip()
    a=a.split(',')
    c=0
    p=0
    y=0
    year=()
    b=[]
    for i in range(1,len(a)):
        c=i
        x.close()
        f=open(filename,encoding='UTF-8')
        z=f.readlines()
        f.close()
        for j in z[1:]:
            j=j.split(',')
            p+=int(j[i])
        b.append(p)
        p=0
        k=max(b)
        l=b.index(k)
        year=int(a[l+1])

    return year
    
 
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
