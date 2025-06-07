def Ex7(file):
    import re
    a=open(file,encoding='UTF-8')
    d={}
    for n in a:
        ln=n.strip().split('.')
        if int(ln[0])==192 and int(ln[1])==168 and int(ln[2])<=255 and int(ln[3])<=255 and 1<=len(ln[2])<=3 and 1<=len(ln[3])<=3 and len(ln)==4:
            d['domestici']+=1
        elif int(ln[0])<=255 and 1<=len(ln[0])<=3 and 1<=len(ln[1])<=3 and int(ln[1])<=255 and int(ln[2])<=255 and int(ln[3])<=255 and 1<=len(ln[2])<=3 and 1<=len(ln[3])<=3 and len(ln)==4:
            d['altri']+=1
        else:
            d['invalidi']+=1
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
