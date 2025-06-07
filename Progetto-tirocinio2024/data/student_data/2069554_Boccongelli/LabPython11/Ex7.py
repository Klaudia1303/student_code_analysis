def Ex7(file):
    f = open(file, 'r', encoding='UTF-8')
    t = f.read().split('\n')
    f.close()
    d = {'invalidi': 0, 'domestici': 0, 'altri': 0}
    for i in range(len(t)):
        p = t[i].split('.')
        c = 0
        for j in p:
            if int(j) >= 0 and int(j) <= 255 and len(j) < 4:
                c += 1
        if c == 4:
            if int(p[0]) == 192 and int(p[1]) == 168:
                d['domestici'] += 1
            else:
                d['altri'] += 1
        else:
            d['invalidi'] += 1
    return d
    
###############################################################################

if __name__ == '__main__':
    from tester import tester_fun
    import re

    counter_test_positivi = 0
    total_tests = 5

    counter_test_positivi += tester_fun(Ex7, ["ip1.txt"] , {'invalidi': 0, 'domestici': 0, 'altri': 5})
    counter_test_positivi += tester_fun(Ex7, ["ip2.txt"] , {'invalidi': 2, 'domestici': 1, 'altri': 2})
    counter_test_positivi += tester_fun(Ex7, ["ip3.txt"] , {'invalidi': 1, 'domestici': 1, 'altri': 3})
    counter_test_positivi += tester_fun(Ex7, ["ip4.txt"] , {'invalidi': 1, 'domestici': 1, 'altri': 3})
    counter_test_positivi += tester_fun(Ex7, ["ip5.txt"] , {'invalidi': 3, 'domestici': 0, 'altri': 2})
    
    print('La funzione',Ex7.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
