def Ex7(file):
    indirizzi={item:0 for item in ['invalidi','domestici','altri']}
    with open(file,encoding='UTF-8') as fin:
        Data=[line.strip() for line in fin.readlines()]
    for line in Data:
        if re.search(r'^((25[0-5]|2[0-4]\d|1\d\d|0?[1-9]\d|0?0?\d)\.?\b){4}$',line):
            if re.search(r'192\.168\.',line):   indirizzi['domestici']+=1
            else:   indirizzi['altri']+=1
        else:   indirizzi['invalidi']+=1
    return indirizzi
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
