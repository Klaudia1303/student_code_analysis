def A_Ex1(l1, l2):
    somma=0
    n=""
    n2=""
    finito=True
    while not finito:
        n=input("Inserisci numero prima lista: ('*' per chiudere la lista) ")
        if n!="*":
            l1.append(n)
        else:
            finito=False
    finito2=True
    while not finito2:
        n2=input("Inserisci numero per la seconda lista: ('*' per chiudere la lista) ")
        if n2!="*":
            l2.append(n2)
        else:
            finito=False
    if len(l1)>len(l2):
        return somma
    else:
        for i in range(len(l1)):
            somma+=int(l1[i])
            somma+=int(l2[i])
            l3.append(somma)
            somma=0
        for i in range(len(l1),len(l2)):
            l3.append(int(l2[i]))
    return l3
l1=[]
l2=[]
l3=[]

 
print(A_Ex1(l1,l2))
    


###############################################################################

"""NON MODIFICARE, codice di testing della funzione"""

if __name__ == '__main__':
    from tester import tester_fun

    """SE NON VOLETE ESEGUIRE UN TEST COMMENTATE LA RIGA RELATIVA CON #"""

    counter_test_positivi = 0
    total_tests = 5

    counter_test_positivi += tester_fun(A_Ex1, [[3,6],[3,4,9]] , [6, 10, 9])
    counter_test_positivi += tester_fun(A_Ex1, [[],[3,4,9]] , [3, 4, 9])
    counter_test_positivi += tester_fun(A_Ex1, [[3,6],[3,4]] ,[6, 10])
    counter_test_positivi += tester_fun(A_Ex1, [[1],[9]] ,[10])
    counter_test_positivi += tester_fun(A_Ex1, [[],[9]] ,[9])

    print('La funzione',A_Ex1.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
