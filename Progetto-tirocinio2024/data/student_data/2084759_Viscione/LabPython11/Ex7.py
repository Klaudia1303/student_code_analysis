def Ex7(file):
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""    
    fin=open(file, encoding="UTF-8")
    testo=fin.read()
    dizionario={}
    dizionario["domestici"]=len(re.findall(r"^192\.168\.(([0-1]?[0-9]?[0-9]?)|(2?[0-5]?[0-5]?))\.(([0-1]?[0-9]?[0-9]?)|(2?[0-5]?[0-5]?))$",testo,re.MULTILINE))    
    dizionario["altri"]=len(re.findall(r"^(([0-1]?[0-9]?[0-9]?)|(2?[0-5]?[0-5]?))\.(([0-1]?[0-9]?[0-9]?)|(2?[0-5]?[0-5]?))\.(([0-1]?[0-9]?[0-9]?)|(2?[0-5]?[0-5]?))\.(([0-1]?[0-9]?[0-9]?)|(2?[0-5]?[0-5]?))$",testo,re.MULTILINE))-dizionario["domestici"]
    dizionario["invalidi"]=len(re.findall(r"^.*$",testo,re.MULTILINE))-dizionario["domestici"]-dizionario["altri"]
    return dizionario
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
