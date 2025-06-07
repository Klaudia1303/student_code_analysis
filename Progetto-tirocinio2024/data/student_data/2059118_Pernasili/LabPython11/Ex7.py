def Ex7(file):
    f = open(file,encoding="UTF8")
    d = {'invalidi':0,'domestici':0,'altri':0}
    for i in f:
         s = "".join(i.strip().split("\n"))
         ss = s.strip().split('.')
         if (ss[0]=='192' and ss[1]=='168') and (int(ss[2])>=0 and int(ss[2])<=255) and (int(ss[3])>=0 and int(ss[3])<=255) and (len(ss[0])<=3 and len(ss[1])<=3 and len(ss[2])<=3 and len(ss[3])<=3):
            d['domestici'] = d['domestici'] + 1
         elif (int(ss[0])>=0 and int(ss[0])<=255) and (int(ss[1])>=0 and int(ss[1])<=255) and (int(ss[2])>=0 and int(ss[2])<=255) and (int(ss[3])>=0 and int(ss[3])<=255) and (len(ss[0])<=3 and len(ss[1])<=3 and len(ss[2])<=3 and len(ss[3])<=3):
            d['altri'] = d['altri'] + 1
         else:
            d['invalidi'] = d['invalidi'] + 1
    f.close()
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
