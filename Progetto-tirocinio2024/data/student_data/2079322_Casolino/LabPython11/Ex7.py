def Ex7(file):
    f=open(file, 'r', encoding='UTF-8')
    s=f.readlines()
    pattern=r'^([0-9][0-9]?[0-9]?)'+'.'+r'([0-9][0-9]?[0-9]?)'+'.'+r'([0-9][0-9]?[0-9]?)'+'.'+r'([0-9][0-9]?[0-9]?)$'
    d={'invalidi':0, 'domestici':0, 'altri':0}
    for i in s:
        mn=re.search(pattern, i)
        if mn==None:
            d['invalidi']+=1
            continue

        if mn.group(1)=='192' and mn.group(2)=='168' and 0<=int(mn.group(3))<=255 and 0<=int(mn.group(4))<=255:
            d['domestici']+=1

        elif 0<=int(mn.group(1))<=255 and 0<=int(mn.group(2))<=255 and 0<=int(mn.group(3))<=255 and 0<=int(mn.group(4))<=255:
            d['altri']+=1

        else:
            d['invalidi']+=1
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
