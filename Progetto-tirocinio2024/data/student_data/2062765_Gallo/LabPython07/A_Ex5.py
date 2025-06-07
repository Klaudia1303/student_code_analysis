def A_Ex5(l):
    l2=[]
    somma_Unicode=0
    for i in range(len(l)):
        for j in range(len(l[i])):
            somma_Unicode+=ord(l[i][j])
        l2.append(somma_Unicode)
        somma_Unicode=0
    return l2

l=[]
s=input("Inserisci stringa: ('*' per terminare)")
while s!="*":
    l.append(s)
    s=input("Inserisci stringa: ('*' per terminare)")

print(A_Ex5(l))

###############################################################################

"""NON MODIFICARE, codice di testing della funzione"""

if __name__ == '__main__':
    from tester import tester_fun

    """SE NON VOLETE ESEGUIRE UN TEST COMMENTATE LA RIGA RELATIVA CON #"""

    counter_test_positivi = 0
    total_tests = 5

    counter_test_positivi += tester_fun(A_Ex5, [["ama","ma","amaca"]], [303,206,499])
    counter_test_positivi += tester_fun(A_Ex5, [[]], [])
    counter_test_positivi += tester_fun(A_Ex5, [["c"]], [99])
    counter_test_positivi += tester_fun(A_Ex5, [["ciao",""]], [412,0])
    counter_test_positivi += tester_fun(A_Ex5, [["",""]], [0,0])

    print('La funzione',A_Ex5.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
