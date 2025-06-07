def Ex4(file):
    f=open(file, "r", encoding="UTF-8")
    f.readline()
    d={}
    for line in f:
        l2=[]
        l=line.strip().split(",")
        oggetto= l[0]
        antenato= l[1]
        erede= l[2]
        
        if oggetto not in d: #aggiungo l'oggetto al dizionario solo se non è presente
            l2.append(antenato)
            d[oggetto]=l2
            
        l2=d.get(oggetto) #ottengo la lista contenuto in d[oggetto]

        if len(l2)==1: #se len(lista)==1 significa che contiene solo il nome del primo antenato
            l2.append(erede) #quindi posso appendere tranquillamente l'erede
            d[oggetto]=l2
            print(d)
        
        elif len(l2)>1:#se len(lista)>1, significa che oltre che al primo antenato, contiene anche un nome di un erede
            if l2[1]==antenato: #vado a modificare la lista solo se l'erede precedente è uguale al nuovo antenato
                l2.remove(l2[1]) #vado a rimuovere il vecchio erede
                l2.append(erede) #vado ad appendere il nuovo erede
                d[oggetto]=l2 #assegno la nuova lista modificata al dizionario
    return d
            
            
        
###############################################################################

"""NON MODIFICARE, codice di testing della funzione"""

if __name__ == '__main__':
    from tester import tester_fun

    counter_test_positivi = 0
    total_tests = 5

    counter_test_positivi += tester_fun(Ex4, ["eredita1.csv"] , {'Anello_di_smeraldi': ['Maria', 'Giorgia'], 'Anello': ['Silvia', 'Paolo']})
    counter_test_positivi += tester_fun(Ex4, ["eredita2.csv"] , {'Anello_di_smeraldi': ['Marco', 'Giorgio'], 'Anello': ['Silvia', 'Sergio']})
    counter_test_positivi += tester_fun(Ex4, ["eredita3.csv"] , {'Anello_di_smeraldi': ['Marco', 'Giorgio'], 'Anello': ['Silvia', 'Sergio'], 'Vaso': ['Anna', 'Sergio']})
    counter_test_positivi += tester_fun(Ex4, ["eredita4.csv"] , {'Anello_di_smeraldi': ['Marco', 'Giorgio'], 'Anello': ['Silvia', 'Giorgio'], 'Vaso': ['Anna', 'Anna']})
    counter_test_positivi += tester_fun(Ex4, ["eredita5.csv"] , {'Anello_di_smeraldi': ['Marco', 'Giorgio'], 'Anello': ['Silvia', 'Sergio'], 'Vaso': ['Sergio', 'Anna']})

    print('La funzione',Ex4.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
