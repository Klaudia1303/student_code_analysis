def Ex7(file):
    f=open(file,encoding='UTF-8')
    d=range(0,255)
    p3=r'\b\d?\d?\d\.\d?\d?\d\.\d?\d?\d\.\d?\d?\d\b'
    p2=r'\b192\.168\.\d?\d?\d\.\d?\d?\d\b'
    d={'invalidi':0,'domestici':0,'altri':0}
    for riga in f:
        r=''.join(riga.strip().split())
        k=r.split('.')
        h=0
        for n in k:
            if 0<=int(n)<=255 and 1<=len(n)<=3:
                continue
            else:
                h=1
        if h==1:
            d['invalidi']+=1
        elif re.match(p2,r):
            d['domestici']+=1
        elif re.match(p3,r):
            d['altri']+=1
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
