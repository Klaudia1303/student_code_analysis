def A_Ex7(s):
    l = [0 for h in range(len(s)) ]
    if len(s)> 0 :
        j = 0
        for i in range (len(s)):
            if s[i]>= 'A' and s[i]<= 'Z':
                l[j] = str (s[i])
                j = j +1
        i = 0
        while i < len(l):
            if l.count(l[i])>1:
                l.remove (l[i])
                i = i -1
            i = i +1
        l.remove(0)
        l.sort()
        return(l)
    else:
        l.clear()
        return(l)

###############################################################################

"""NON MODIFICARE, codice di testing della funzione"""

if __name__ == '__main__':
    from tester import tester_fun

    """SE NON VOLETE ESEGUIRE UN TEST COMMENTATE LA RIGA RELATIVA CON #"""

    counter_test_positivi = 0
    total_tests = 5

    counter_test_positivi += tester_fun(A_Ex7, ['cIAo MAmMa'],['A','I','M'])
    counter_test_positivi += tester_fun(A_Ex7, ['3219'], [])
    counter_test_positivi += tester_fun(A_Ex7, ['aG2Hl'], ['G','H'])
    counter_test_positivi += tester_fun(A_Ex7, ['PPq&/&90PQ'], ['P','Q'])
    counter_test_positivi += tester_fun(A_Ex7, [''], [])

    print('La funzione',A_Ex7.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
