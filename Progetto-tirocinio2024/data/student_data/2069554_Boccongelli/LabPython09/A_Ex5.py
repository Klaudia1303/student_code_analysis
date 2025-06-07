def A_Ex5(filename,oggetto):
    f = open(filename, 'r', encoding="UTF-8")
    t = f.read().split('\n')
    f.close()
    for i in range(1, len(t)):
        s = t[i].split(',')
        if (s != [''] and s[0] == oggetto):
            if (max(s[1:]) == s[1]):
                return int(t[0].split(',')[s.index(str(s[1]))])
            else:
                m = 0
                a = 0
                for j in range(2, len(s)):
                    crescita = int(s[j]) - int(s[j - 1])
                    if (crescita > m):
                            m = crescita
                            a = int(t[0].split(',')[j])
                    if (crescita == m):
                            a = max(a, int(t[0].split(',')[j]))
                return a
                            
            

###############################################################################

"""NON MODIFICARE, codice di testing della funzione"""

if __name__ == '__main__':
    from tester import tester_fun

    counter_test_positivi = 0
    total_tests = 5

    counter_test_positivi += tester_fun(A_Ex5, ['Vendite1.csv','Giubbotto'] , 2012)
    counter_test_positivi += tester_fun(A_Ex5, ['Vendite1.csv','Zaino'] , 2010)
    counter_test_positivi += tester_fun(A_Ex5, ['Vendite2.csv','Maglione'] , 2012)
    counter_test_positivi += tester_fun(A_Ex5, ['Vendite2.csv','Zaino'] , 2013)
    counter_test_positivi += tester_fun(A_Ex5, ['Vendite3.csv','Giubbotto'] , 2013)

    print('La funzione',A_Ex5.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
