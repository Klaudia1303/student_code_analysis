def Ex7(file):
    d={'invalidi':0,'domestici':0,'altri':0}
    file=open(file, encoding='UTF-8')
    for riga in file:
        patterng= r'^((25[0-5]|2[0-4]\d|1\d\d|0?[1-9]\d|0?0?\d)\.?\b){4}$'
        patternd= r'192\.168\.'
        if re.search(patterng, riga):
            if re.search(patternd, riga):
                if 'domestici' in d:
                    d['domestici']+=1
            else:
                 if 'altri' in d:
                    d['altri']+=1
        else:
            if 'invalidi' in d:
                d['invalidi']+=1
    file.close()
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
