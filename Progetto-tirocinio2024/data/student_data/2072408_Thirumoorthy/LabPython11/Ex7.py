def Ex7(file):
    d={'invalidi':0,'altri':0,'domestici':0}
    f=open(file,encoding='UTF-8')
    for line in f.readlines():
        line=line.strip()
        if len([int(i) for i in line.split('.') if int(i)>=0 and 255>=int(i)])<4:
            d['invalidi']+=1
            continue
        if re.match('^192.168.[0-9]{1,3}\.[0-9]{1,3}$',line):
            d['domestici']+=1
        elif re.match('^[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}$',line):
            d['altri']+=1
        else:
            d['invalidi']+=1

            

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
