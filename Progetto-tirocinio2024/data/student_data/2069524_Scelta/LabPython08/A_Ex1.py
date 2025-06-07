def A_Ex1(l):
    piùocc=''
    frequenza_generale=-1
    
    for s in l:
        freq=0
        candidate=s[0]
        for ch in s:
            accum=0
            if ch.isupper() or not ch.isalpha():
                continue
            
            i=0
            while i<len(l):
                if ch in l[i]:
                    accum+=1
                i+=1
            
            if accum>freq:
                freq=accum
                candidate=ch
        
        if freq>frequenza_generale:
            piùocc=candidate
            frequenza_generale=freq
        elif freq==frequenza_generale:
            piùocc=max(candidate,piùocc)
    
    return piùocc
        
    
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
