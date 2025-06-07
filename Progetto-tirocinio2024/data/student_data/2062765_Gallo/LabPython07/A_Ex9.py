def A_Ex9(l):
    l2=[]
    conta=0
    s2=""
    for i in range(len(l)):
        for j in range(len(l[i])):
            if l[i].count(l[i][j])>conta:
                s2=l[i][j]
                conta+=l[i].count(l[i][j])
            elif l[i].count(l[i][j])==conta:
                
                if ord(l[i][j])<ord(s2):
                    s2=l[i][j]
                    conta+=l[i].count(l[i][j])-1
        conta=0
        l2.append(s2)
        s2=""
    return l2
l=[]
s=input("Inserisci stringa (premi invio per terminare): ")
while s!="":
    l.append(s)
    s=input("Inserisci stringa (premi invio per terminare): ")

print(A_Ex9(l))
    

###############################################################################

"""NON MODIFICARE, codice di testing della funzione"""

if __name__ == '__main__':
    from tester import tester_fun

    """SE NON VOLETE ESEGUIRE UN TEST COMMENTATE LA RIGA RELATIVA CON #"""

    counter_test_positivi = 0
    total_tests = 5

    counter_test_positivi += tester_fun(A_Ex9, [['amaca','amaranto','rosso']], ['a','a','o'])
    counter_test_positivi += tester_fun(A_Ex9, [['osso','assolato','alto']], ['o','a','a'])
    counter_test_positivi += tester_fun(A_Ex9, [['stringa','a','bbbbcccc','dado']], ['a','a','b','d'])
    counter_test_positivi += tester_fun(A_Ex9, [['fosso','dosso','rosso','fosso']], ['o', 'o', 'o', 'o'])
    counter_test_positivi += tester_fun(A_Ex9, [['ciao mamma','ciao ']], ['a', ' '])

    print('La funzione',A_Ex9.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
