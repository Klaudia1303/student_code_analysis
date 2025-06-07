def Ex7(file):
    fin=open(file,encoding='UTF-8')
    d={'invalidi':0,'domestici':0,'altri':0}
    riga=fin.readline()
    while len(riga)>0:
        riga=riga.strip().split('.')
        if int(riga[0])==192 and len(riga[0])<=3  and int(riga[1])==168 and len(riga[1])<=3 and int(riga[2])<=255 and len(riga[2])<=3 and int(riga[3])<=255 and len(riga[3])<=3:
            d['domestici']+=1
        elif int(riga[0])<=255 and len(riga[0])<=3 and int(riga[1])<=255 and len(riga[1])<=3 and int(riga[2])<=255and len(riga[2])<=3 and int(riga[3])<=255 and len(riga[3])<=3:
            d['altri']+=1
        else:
            d['invalidi']+=1
        riga=fin.readline()
    fin.close()
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
