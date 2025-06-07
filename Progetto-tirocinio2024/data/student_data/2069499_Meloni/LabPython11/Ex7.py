def Ex7(file):
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""
    testo=open(file,encoding='UTF-8')
    
    pattern_dom=r'(\b192\.168\.)((25[0-5])|(2[0-4]\d)|(1\d\d)|(0?(\d)?\d))\.((25[0-5])|(2[0-4]\d)|(1\d\d)|(0?(\d)?\d))\b'
    
    pattern_altri=r'\b((25[0-5])|(2[0-4]\d)|(1\d\d)|(0?(\d)?\d))\.((25[0-5])|(2[0-4]\d)|(1\d\d)|(0?(\d)?\d))\.((25[0-5])|(2[0-4]\d)|(1\d\d)|(0?(\d)?\d))\.((25[0-5])|(2[0-4]\d)|(1\d\d)|(0?(\d)?\d))\b'
    
    diz={'invalidi':0, 'domestici':0, 'altri':0}

    for indirizzo_ip in testo:
        if re.match(pattern_dom,indirizzo_ip):
            diz['domestici']+=1
        elif re.match(pattern_altri,indirizzo_ip):
            diz['altri']+=1
        else:
            diz['invalidi']+=1
    return(diz)
    
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
