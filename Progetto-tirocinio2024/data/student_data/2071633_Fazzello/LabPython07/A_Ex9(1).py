##Scrivere una funzione che prende in ingresso una lista l contenente stringhe non vuote e 
##restituisce la lista dei caratteri più frequenti di ciascuna stringa. Se una stringa ha più di un carattere 
##più frequente, l’insieme deve contenere il più piccolo carattere nell’ordine Unicode. Ad esempio, se 
##l= ['amaca', 'amaranto', 'rosso'] allora la funzione deve restituire ['a', 'a', 'o']

def A_Ex9(l):
    l1=[]
    s=1
    y='ÿ'
    for i in range(len(l)):
        for j in range(len(l[i])):
            x=l[i].count(l[i][j])
            x=int(x)
            if x>=s and l[i][j]<y:
                s=x
                y=l[i][j]
        l1.append(y)
        s=1
    return l1

#############################################################################

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

