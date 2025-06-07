def A_Ex6(l1, l2):
    l3=[]
    for i in range(len(l1)):
        if l1[i] not in l2:
            l3.append(int(l1[i]))
    l3.sort()

    return l3


l1=[]
l2=[]
n1=input("Inserisci intero (premi invio per terminare) : ")
while n1!="":
    l1.append(int(n1))
    n1=input("Inserisci intero (premi invio per terminare): ")
n2=input("Inserisci secondo intero (premi invio per terminare) : ")
while n2!="":
    l2.append(int(n2))
    n2=input("Inserisci secondo intero (premi invio per terminare) : ")

print(A_Ex6(l1,l2))



###############################################################################

"""NON MODIFICARE, codice di testing della funzione"""

if __name__ == '__main__':
    from tester import tester_fun

    """SE NON VOLETE ESEGUIRE UN TEST COMMENTATE LA RIGA RELATIVA CON #"""

    counter_test_positivi = 0
    total_tests = 5

    counter_test_positivi += tester_fun(A_Ex6, [[1, 3, 2, 1, -5],[1, 3]],[-5, 2])
    counter_test_positivi += tester_fun(A_Ex6, [[1, 3, 2, 1, -5],[1, 1, 1]],[-5, 2, 3])
    counter_test_positivi += tester_fun(A_Ex6, [[10, 1, 10, 1, 2],[10, 1, 2]],[])
    counter_test_positivi += tester_fun(A_Ex6, [[],[1, 1, 1]],[])
    counter_test_positivi += tester_fun(A_Ex6, [[100, 12, -2, -1, -2],[]],[-2, -2, -1, 12, 100])

    print('La funzione',A_Ex6.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
