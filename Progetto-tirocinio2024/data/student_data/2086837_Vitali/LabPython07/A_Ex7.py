def A_Ex7(s):
    l=[]
    x=0
    s=s.strip()
    for i in range(len(s)):
        if s[i].isalpha()==True:
            if ord(s[i])==ord(s[i].upper()):
                if l.count(s[i])==0:
                    l.insert(x,s[i])
                    x+=1
    l.sort()
    return l
            
            

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
