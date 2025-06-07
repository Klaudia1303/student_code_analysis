def A_Ex1(l):
    chars = ''

    # crea una stringa contenente i caratteri che compaiono in ogni stringa. i set
    # impediscono che più caratteri uguali della stessa parola siano presi in considerazione
    for w in l:
        wchars = {c for c in w if 'a' <= c <= 'z'}
        chars += ''.join([e for e in wchars])
    
    # c_ret è una tupla contente il carattere che compare più volte e il # di volte
    c_ret = ('', 0)

    # si cerca il carattere che appare più volte nella stringa precedente
    for c in set(chars):
        if chars.count(c) > c_ret[1]:
            c_ret = (c, chars.count(c))

        elif chars.count(c) == c_ret[1] and c > c_ret[0]:
            c_ret = (c, c_ret[1])
        
    return c_ret[0]
    

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
