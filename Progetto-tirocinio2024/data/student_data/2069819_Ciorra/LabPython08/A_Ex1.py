from tester import tester_fun

def A_Ex1(l):
    maxCar=''
    maxFreq=0
    for c in 'abcdefghijklmnopqrstuvwyz':
        cont=0
        for s in l:
            if c in s:
                cont+=1
        if cont > maxFreq:
            maxFreq=cont
            maxCar=c
        elif cont == maxFreq and c > maxCar:
            maxCar=c
    return maxCar
            
            
## la seguente versione funziona per qualunque tipo di carattere
## non solo per caratteri alfabetici minuscoli
##
##
##def A_Ex1(l):
##    ret = ''
##    max = 0
##    visited = ""
##    for word1 in l:
##        for c in word1:
##            if c not in visited: #and c.islower(): #decommentare c.islower() e levare i : dopo visited se
##                                                   #ci si vuole limitare ai soli caratteri alfabetici minuscoli
##                counterC = 0
##                for word2 in l:
##                    if c in word2:
##                        counterC += 1
##                visited += c
##                if counterC > max:
##                    max = counterC
##                    ret = c
##                if counterC == max and c > ret:
##                    max = counterC
##                    ret = c
##    return ret
###############################################################################

"""NON MODIFICARE IL SEGUENTE CODICE (codice di test della funzione)"""

if __name__ == '__main__':
    from tester import tester_fun

    """SE NON VOLETE ESEGUIRE UN TEST COMMENTATE LA RIGA RELATIVA CON #"""

    counter_test_positivi = 0
    total_tests = 10

    counter_test_positivi += tester_fun(A_Ex1, [["casa", "senape", "ketchup", "pasta"]] , "s")
    counter_test_positivi += tester_fun(A_Ex1, [["a", "b", "b", "a", "a", "a", "a"]] , "a")
    counter_test_positivi += tester_fun(A_Ex1, [["1fI", "1FI", "1FI", "1FI","1FI" ]] , "f")
    counter_test_positivi += tester_fun(A_Ex1, [["conte", "dpcm"]] , "c")
    counter_test_positivi += tester_fun(A_Ex1, [["Zlatan", "Ibraimovich", "Cristiano", "Ronaldo", "Francesco", "Totti"]] , "o")
    
    counter_test_positivi += tester_fun(A_Ex1, [["z", "a", "a", "z"]] , "z")
    counter_test_positivi += tester_fun(A_Ex1, [["A", "A", "A", "b"]] , "b")
    counter_test_positivi += tester_fun(A_Ex1, [["a", "a", "a", "b"]] , "a")
    counter_test_positivi += tester_fun(A_Ex1, [["1", "123", "11_a_22", "123c456","wwaww"]] , "a")
    counter_test_positivi += tester_fun(A_Ex1, [["Zb"]] , "b")

    print('La funzione',A_Ex1.__name__,'ha superato',counter_test_positivi,'test su',total_tests)

