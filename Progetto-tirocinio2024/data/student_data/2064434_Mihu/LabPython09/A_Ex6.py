def A_Ex6(filename):
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""
    f=open(filename, encoding="UTF-8")
    s=f.readline()
    s=s.strip()
    s=s.split(",")
    colonna= 0
    somma=0
    sm=0
    anno=()
    A=[]
    for i in range(1,len(s)):
        colonna = i
        f.close()
        fin=open(filename, encoding="UTF-8")
        t=fin.readlines()
        fin.close()
        for j in t[1:]:
            j=j.split(",")
            somma +=int(j[i])
        A.append(somma)
        somma=0
        y=max(A)
        x=A.index(y)
        anno= int(s[x+1])
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
