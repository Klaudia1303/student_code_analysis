def Ex7(file):
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""
    x={'invalidi':0,'domestici':0,'altri':0}
    f=open(file,encoding='UTF-8')
    p=r'\b(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})\b' 
    for l in f:
        match=re.match(p,l)
        if match:
            if int(match.group(3))<=255 and int(match.group(4))<=255:
                if match.group(1)=='192' and match.group(2)=='168':
                    x['domestici']+=1
                elif int(match.group(1))<=255 and int(match.group(2))<=255:
                    x['altri']+=1
                else:
                    x['invalidi']+=1
            else:
                    x['invalidi']+=1
        else:
            x['invalidi'] += 1

    return x
    
    
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
