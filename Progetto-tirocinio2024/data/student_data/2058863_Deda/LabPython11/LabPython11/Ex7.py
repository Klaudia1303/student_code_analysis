def Ex7(file):
    f=open(file, 'r', encoding='UTF-8')
    x=f.read()
    import re
    patternaltri=r'\b(?:([0-1]?[0-9]?[0-9]|[2][0-4][0-9]|[2][5][0-5]))\.(?:([0-1]?[0-9]?[0-9]|[2][0-4][0-9]|[2][5][0-5]))\.(?:([0-1]?[0-9]?[0-9]|[2][0-4][0-9]|[2][5][0-5]))\.(?:([0-1]?[0-9]?[0-9]|[2][0-4][0-9]|[2][5][0-5]))\b'
    patterndomestici=r'\b(192)\.(168)\.(?:([0-1]?[0-9]?[0-9]|[2][0-4][0-9]|[2][5][0-5]))\.(?:([0-1]?[0-9]?[0-9]|[2][0-4][0-9]|[2][5][0-5]))\b'
    altri=re.findall(patternaltri, x, re.IGNORECASE)
    domestici=re.findall(patterndomestici, x, re.IGNORECASE)
    d={}
    print(altri, domestici)
    p=len(altri)-len(domestici)
    d['altri']=p
    d['domestici']=len(domestici)
    d['invalidi']=len(x.strip().split())-len(altri)
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
