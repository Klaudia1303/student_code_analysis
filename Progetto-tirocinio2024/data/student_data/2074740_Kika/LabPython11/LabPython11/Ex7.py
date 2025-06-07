def Ex7(file):
    #"""MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""
    f=open(file,encoding='UTF-8')
    d={}
    tipologia=['invalidi','domestici','altri']
    for i in tipologia:
        d[i]=0
    #ho il dizionario
    for riga in f:
        riga=riga.strip().split('.')
        for num in riga:
            if 1<=len(num)<=3 and 0<=int(num)<=255:
                valido='si'
            else:
                d['invalidi']+=1
                valido='no'
                break
        if (int(riga[0])==192 and int(riga[1])==168 and valido=='si'):
            d['domestici']+=1
        if ((int(riga[0])!=192 or int(riga[1])!=168) and valido=='si'):
            d['altri']+=1
    f.close()
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
