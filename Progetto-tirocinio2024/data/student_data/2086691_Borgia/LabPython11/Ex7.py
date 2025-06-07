def Ex7(file):
    import re
    d={}
    d['invalidi']=0
    d['domestici']=0
    d['altri']=0
    w='192'
    v='168'
    k1=0
    k2=0
    k3=0
    f=open(file,encoding="UTF-8")
    pattern_ip_domestici=w+r'([^\t\n\r\f\vA-Za-z0-9_])'+v+r'\1[0-255]\1[0-255]'
    pattern_ip_altri=r'[0-999]([^\t\n\r\f\vA-Za-z0-9_])[0-999]\1[0-999]\1[0-999]'
    for row in f:
        row=row.strip()
        domestici=re.search(pattern_ip_domestici,row)
        altri=re.search(pattern_ip_altri,row)
        if domestici or altri:
            k3+=1
            d['invalidi']=k3
        elif altri:
            k2+=1
            d['altri']=k2
        else:
            k1+=1
            d['domestici']=k1
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
