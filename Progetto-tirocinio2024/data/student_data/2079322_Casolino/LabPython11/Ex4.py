def Ex4(file):
    f=open (file, "r", encoding-"UTF-8")
    f.readline ()
    d={}
    for line in f:
        lista=list()
        l=line.strip().split(",")
        oggetto=l[0]
        antenato=l[1]
        erede=l[2]

        if oggetto not in d: #aggiungo l'oggetto al dizionario solo se non è presente
            lista.append(antenato)
            d[oggetto]=lista

        lista=d.get(oggetto) #ottengo la lista contenuto in d[oggetto]
        if len(lista)==1: #se len(lista)==1 significa che contiene solo il nome del primo antenato
            lista.append (erede) #quindi posso appendere tranquillamente l'erede
            d[oggetto]=lista
        elif len(lista)>1:#se len(lista)>1, significa che oltre che al primo antenato, contiene anche un nome di un erede
            if lista[1]==antenato: #vado a modificare la lista solo se l'erede precedente è uguale al nuovo antenato
                lista.remove(lista[1]) #vado a rimuovere il vecchio erede
                lista.append(erede) #vado ad appendere il nuovo erede
                d[oggetto]=lista #assegno la nuova lista modificata al dizionario
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
