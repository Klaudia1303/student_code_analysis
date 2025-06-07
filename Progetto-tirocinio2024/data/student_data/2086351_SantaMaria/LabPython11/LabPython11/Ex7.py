def Ex7(file):
    import re
    risultato={'invalidi':0,'domestici':0,'altri':0}
    pattern=r'[0-9]{3},[0-9]{3},[0-9]{3}'
    fin=open(file,encoding='utf-8')
    ver=False
    for riga in fin:
        line=riga.strip().split('.')
        for i in line:
            if int(i)>255 or len(str(i))>3:
                ver=True
        if ver:
            risultato['invalidi']+=1
        elif int(line[0])==192 and int(line[1])==168:
            risultato['domestici']+=1
        else:
            risultato['altri']+=1
        ver=False
    return risultato
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
