#Scrivere una funzione che prende in ingresso una lista l di stringhe
#e un intero non negativo n e restituisce la stringa composta, in ordine,
#da tutti i caratteri con indice n di tutte le stringhe della lista.
#Se in una stringa in l non c’è il carattere di indice n
#(perché la stringa è troppo corta), la funzione deve inserire il carattere ‘!’.
#Se la lista in ingresso è vuota, la funzione deve restituire la stringa vuota.
#Ad esempio, se l vale [‘tanto’, ‘va’, ‘la’, ‘gatta’, ‘al’, ‘lardo’]
#e n vale 3 la funzione deve restituire la stringa ‘t!!t!d’


def A_Ex3(l,n):
    s=''
    if len(l)==0:
        return s
    for i in l:
        if n>=len(i):
            s+='!'
        else:
            s+=i[n]
    return s


###############################################################################

"""NON MODIFICARE, codice di testing della funzione"""

if __name__ == '__main__':
    from tester import tester_fun

    """SE NON VOLETE ESEGUIRE UN TEST COMMENTATE LA RIGA RELATIVA CON #"""

    counter_test_positivi = 0
    total_tests = 5

    counter_test_positivi += tester_fun(A_Ex3, [['tanto', 'va', 'la', 'gatta', 'al', 'lardo'], 3], 't!!t!d')
    counter_test_positivi += tester_fun(A_Ex3, [['tanto', 'va', 'la', 'gatta', 'al', 'lardo', 'che', 'ci', 'lascia', 'lo', 'zampino'], 4], 'o!!a!o!!i!i')
    counter_test_positivi += tester_fun(A_Ex3, [['nel', 'mezzo', 'del', 'cammin', 'di', 'nostra', 'vita', 'mi', 'ritrovai'], 6], '!!!!!!!!a')
    counter_test_positivi += tester_fun(A_Ex3, [['nel', 'mezzo', 'del', 'cammin', 'di', 'nostra', 'vita', 'mi', 'ritrovai'], 0], 'nmdcdnvmr')
    counter_test_positivi += tester_fun(A_Ex3, [[], 0],'')

    print('La funzione',A_Ex3.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
