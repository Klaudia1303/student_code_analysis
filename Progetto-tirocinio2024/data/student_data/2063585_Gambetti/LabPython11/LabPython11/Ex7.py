def Ex7(file):
    f=open(file,encoding='UTF-8')
    f=f.readlines()
    d={}
    d['invalidi']=0
    d['domestici']=0
    d['altri']=0
    for elem in f:
        elem=elem.strip().split('.')
        if len(elem)==4:
            if 1<=len(elem[0])<=3 and 1<=len(elem[1])<=3 and 1<=len(elem[2])<=3 and 1<=len(elem[3])<=3:
                if 0<=int(elem[0])<=255 and 0<=int(elem[1])<=255 and 0<=int(elem[2])<=255 and 0<=int(elem[3])<=255:
                    if elem[0]=='192' and elem[1]=='168':
                        d['domestici']+=1
                    else:
                        d['altri']+=1
                else:
                    d['invalidi']+=1
            else:
                d['invalidi']+=1
        else:
            d['invalidi']+=1
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
