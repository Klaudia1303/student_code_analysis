def Ex7(file):
    file = open(file, encoding='UTF-8')
    l =[]
    for elem in file:
        l.append(elem.strip())
    d = {}
    d['invalidi'] = 0
    d['domestici'] = 0
    d['altri'] = 0
    for elem in l :
        if re.match(r'(\b(2[0-5][0-5][.]|1[0-9][0-9][.]|[0]?[0-9]?[0-9][.])){3}(2[0-5][0-5]\b|1[0-9][0-9]\b|[0]?[0-9]?[0-9]\b)', elem)!= None :
            if re.match (r'192[.]168[.](2[0-5][0-6][.]|1[0-9][0-9][.]|[0]?[0-9]?[0-9][.])(2[0-5][0-6]\b|1[0-9][0-9]\b|[0]?[0-9]?[0-9]\b)',elem) != None:
                d['domestici'] = d ['domestici'] + 1
            else:
                d['altri'] = d['altri']+1
        else:
            d['invalidi'] = d['invalidi'] + 1
    return(d)
        


    
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
