##Scrivere una funzione che prende in ingresso una lista l non vuota di stringhe e calcola quale
##carattere alfabetico minuscolo (‘a’-‘z’) compare in più stringhe. Se ci sono più caratteri che compaiono
##lo stesso numero di volte si scelga quello alfabeticamente più grande. Ad esempio, se l = [‘casa’,
##‘senape’, ‘ketchup’, ‘pasta’], allora il carattere da restituire è ‘s’ che compare in 3 stringhe ed è più
##grande di ‘a’ e ‘p’, che anche compaiono in 3 stringhe.

def A_Ex1(l):
    x=0
    y=''
    for i in range(len(l)):
        for j in range(len(l[i])):
            if l[i][j].islower()==True:
                for k in range(len(l[i])):
                    if l[i].count(l[i][j])>=x and l[i][j]>y:
                        x=x+l[i].count(l[i][j])
                        y=l[i][j]
    return y
                
    

###############################################################################

"""NON MODIFICARE IL SEGUENTE CODICE (codice di test della funzione)"""

if __name__ == '__main__':
    from tester import tester_fun

    """SE NON VOLETE ESEGUIRE UN TEST COMMENTATE LA RIGA RELATIVA CON #"""

    counter_test_positivi = 0
    total_tests = 5

    counter_test_positivi += tester_fun(A_Ex1, [["casa", "senape", "ketchup", "pasta"]] , "s")
    counter_test_positivi += tester_fun(A_Ex1, [["a", "b", "b", "a", "a", "a", "a"]] , "a")
    counter_test_positivi += tester_fun(A_Ex1, [["1fI", "1FI", "1FI", "1FI","1FI" ]] , "f")
    counter_test_positivi += tester_fun(A_Ex1, [["conte", "dpcm"]] , "c")
    counter_test_positivi += tester_fun(A_Ex1, [["Zlatan", "Ibraimovich", "Cristiano", "Ronaldo", "Francesco", "Totti"]] , "o")


    print('La funzione',A_Ex1.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
