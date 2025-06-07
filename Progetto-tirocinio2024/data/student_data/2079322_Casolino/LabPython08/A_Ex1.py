#Scrivere una funzione che prende in ingresso una lista l non vuota di stringhe e
#calcola quale carattere alfabetico minuscolo (‘a’-‘z’) compare in più stringhe.
#Se ci sono più caratteri che compaiono lo stesso numero di volte si scelga
#quello alfabeticamente più grande. Ad esempio, se l = [‘casa’, ‘senape’,
#‘ketchup’, ‘pasta’], allora il carattere da restituire è ‘s’ che compare
#in 3 stringhe ed è più grande di ‘a’ e ‘p’, che anche compaiono in 3 stringhe.

def A_Ex1(l):
    max=0
    char=96
    for i in range(97,123):      #l'alfabeto dalla a alla z in Unicode corrisponde ai numeri da 97 a 123
        c=0
        for j in range(len(l)):  #posizione della stringa della lista 
            if (chr(i) in l[j]): #controllo se il carattere dell'alfabeto sta nella stringa della lista nella posizione j
                c+=1             #conto quante volta il carattere è presente nella lista
        if (c>max) or (c==max and i>char): #devo controllare il carattere più ricorrente e se due caratteri hanno la stessa
                                           #ricorrenza conservo come nuovo carattere di confronto quello alfabeticamente più
                                           #grande
            max=c  #conservo un nuovo massimo da controllare (quante volte si ripete un carattere)
            char=i #conservo un nuovo carattere per il confronto finale
    return chr(char) #ritorna il carattere che più si ripete

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
