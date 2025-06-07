def A_Ex6(filename):
    f=open(filename, encoding='UTF-8')
    l=[]
    l1=[]
    a=0
    b=0
    c=0
    for riga in f:
        l.append(riga)
    for i in range(len(l)):
        riga=l[i].strip().split(',')
        l1.append(riga)
    for i in range(1,len(l1)):
        a+=int(l1[i][1])
        b+=int(l1[i][2])
        c+=int(l1[i][3])
    if a>b and a>b:
        return int(l1[0][1])
    elif b>a and b>c:
        return int(l1[0][2])
    elif c>a and c>b:
        return int(l1[0][3])
    elif a==b:
        return int(max(l1[0][1],l1[0][2]))
    elif a==c:
        return int(max(l1[0][1],l1[0][3]))
    elif b==c:
        return int(max(l1[0][2],l1[0][3]))
        
    








    
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""
 
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
