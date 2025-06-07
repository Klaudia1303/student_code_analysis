#import re
def Ex5(file):
    fin=open(file,encoding='UTF-8')
    fileRead=fin.read()
    dictionary={}
    pattern=[r'[A-ZA-Z]\d\d\d[A-ZA-Z]',r'[A-ZA-Z]\d\d\d\d\d',r'\b[A-Z0-9]{5}\b',r'\b[A-Z0-9]{6}\b']
    items=['auto','moto','ciclomotore1','ciclomotore2','errata']
    for j in items:
        dictionary[j]=dictionary.get(j,0)
    for i in range(len(pattern)):
        dictionary[items[i]]=len(re.findall(pattern[i],fileRead))
        
    dictionary['errata']=len(fileRead.strip().split())-sum(dictionary.values())
    
    return dictionary
        
      
###############################################################################

if __name__ == '__main__':
    from tester import tester_fun
    import re

    counter_test_positivi = 0
    total_tests = 5

    counter_test_positivi += tester_fun(Ex5, ["targhe1.txt"] , {'auto': 2, 'moto': 1, 'ciclomotore1': 1, 'ciclomotore2': 1, 'errata': 1})
    counter_test_positivi += tester_fun(Ex5, ["targhe2.txt"] , {'auto': 2, 'moto': 1, 'ciclomotore1': 1, 'ciclomotore2': 1, 'errata': 2})
    counter_test_positivi += tester_fun(Ex5, ["targhe3.txt"] , {'auto': 3, 'moto': 1, 'ciclomotore1': 1, 'ciclomotore2': 1, 'errata': 3})
    counter_test_positivi += tester_fun(Ex5, ["targhe4.txt"] , {'auto': 3, 'moto': 1, 'ciclomotore1': 1, 'ciclomotore2': 1, 'errata': 4})
    counter_test_positivi += tester_fun(Ex5, ["targhe5.txt"] , {'auto': 2, 'moto': 1, 'ciclomotore1': 1, 'ciclomotore2': 1, 'errata': 5})
    
    print('La funzione',Ex5.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
