def Ex7(file):
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""
    with open(file, encoding='utf-8') as f:
        data = [line.strip() for line in f.readlines()]
        out = {'invalidi': 0,'domestici': 0,'altri': 0}
        for ip in data:
            _ip = ip.split('.')
            if all([0 <= len(n) <= 3 for n in _ip]):
                _ip = list(map(int, _ip))
                if all([(0 <= n <= 255) for n in _ip]):
                    if _ip[0] == 192 and _ip[1] == 168:
                        out['domestici'] += 1
                    else:
                        out['altri'] += 1
                else:
                    out['invalidi'] += 1
            else: out['invalidi'] += 1
    return out
    
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
