def Ex7(file):
    f=open(file)
    r=0
    for riga in f:
        r+=1
    f=open(file).read()
    d={}
    pattern='^192\.168\.([0-9]{1,3})\.([0-9]{1,3})$'
    for m in re.finditer(pattern,f,re.MULTILINE):
        if int(m.group(1))<256 and int(m.group(2))<256:
            d['domestici']=d.get('domestici',0)+1
    d['domestici']=d.get('domestici',0)
    pattern='^([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})$'
    validi=0
    for m in re.finditer(pattern,f,re.MULTILINE):
        if int(m.group(1))<256 and int(m.group(2))<256 and int(m.group(3))<256 and int(m.group(4))<256:
            validi+=1
    d['invalidi']=r-validi
    d['altri']=validi-d['domestici']
    print(validi)
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
