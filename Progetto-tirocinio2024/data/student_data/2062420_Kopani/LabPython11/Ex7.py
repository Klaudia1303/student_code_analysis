def Ex7(file):
    f=open(file,encoding='UTF-8')
    d={'invalidi': 0, 'domestici': 0, 'altri': 0}
    pattern=r'\b([0-9]*)\.([0-9]*)\.([0-9]*)\.([0-9]*)\b'
    s=f.read()
    i=re.finditer(pattern,s)
    f.close()
    for m in i:
    	g1=m.group(1)
    	g2=m.group(2)
    	g3=m.group(3)
    	g4=m.group(4)
    	n1=int(g1)
    	n2=int(g2)
    	n3=int(g3)
    	n4=int(g4)
    	if n1>255 or n2>255 or n3>255 or n4>255 or len(g1)>3 or len(g2)>3 or len(g3)>3 or len(g4)>3:
    		d['invalidi']+=1
    	elif n1==192 and n2==168 and n3<256 and n4<256:
    		d['domestici']+=1
    	else:
    		d['altri']+=1
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
