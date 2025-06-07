def Ex7(file):
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""
    d = {'invalidi':0,
         'domestici': 0,
         'altri': 0}
    patt =  r'^([0-2]?[0-9]?[0-9])\.([0-2]?[0-9]?[0-9])\.([0-2]?[0-9]?[0-9])\.([0-2]?[0-9]?[0-9])$'
    with open (file, encoding='UTF-8') as f:
        for ip in f:
            m = re.match(patt, ip)
            if m:
                if (int(m.group(1)), int(m.group(2))) == (192, 168) and 0<=(max(int(m.group(3)), int(m.group(4))))<=255:
                    d['domestici']+=1
                    continue
                if 0<= max(int(m.group(1)), int(m.group(2)), int(m.group(3)), int(m.group(4)))<=255:
                    d['altri'] += 1
                    continue
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
