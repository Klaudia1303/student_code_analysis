def Ex7(file):

    reti = {'invalidi': 0, 'altri': 0, 'domestici': 0}

    with open(file, encoding = 'UTF-8') as f:

        lines = f.readlines()

        for line in lines:
            line = line.strip()
            if len([int(x) for x in line.split('.') if 0<=int(x)<=255]) < 4:
                reti['invalidi'] += 1
                continue
            if re.match('^192.168.[0-9]{1,3}\.[0-9]{1,3}$',line):
                reti['domestici'] += 1
            elif re.match('^[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}$',line):
                reti['altri'] += 1
            else:
                reti['invalidi'] += 1

    return reti

        
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
