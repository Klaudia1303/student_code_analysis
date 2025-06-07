def Ex7(file):
    x = open(file,'r',encoding = 'UTF-8')
    d = {}
    d['invalidi'] = 0
    d['domestici'] = 0
    d['altri'] = 0

    pattern = r'^((0?0?[0-9])|(0?[0-9][0-9])|(1[0-9][0-9])|(2[0-4][0-9])|(25[0-5]))\.((0?0?[0-9])|(0?[0-9][0-9])|(1[0-9][0-9])|(2[0-4][0-9])|(25[0-5]))\.((0?0?[0-9])|(0?[0-9][0-9])|(1[0-9][0-9])|(2[0-4][0-9])|(25[0-5]))\.((0?0?[0-9])|(0?[0-9][0-9])|(1[0-9][0-9])|(2[0-4][0-9])|(25[0-5]))$'
    for i in x:
        a = re.search(pattern, i, flags = re.MULTILINE)
        if a:
            if a.group(1) == '192' and a.group(7) == '168':
                d['domestici'] = d['domestici']+1
            else:
                d['altri'] = d['altri']+1
        else:
            d['invalidi'] = d['invalidi']+1
            
    x.close()
    return d
                    
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""    
    
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
