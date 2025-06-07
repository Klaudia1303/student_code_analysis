#Ex4(file): Scrivere una funzione Python che prende in ingresso il nome di un file csv contenente tutte le 
#eredità di una famiglia nel seguente formato: 
#Oggetto,Antenato,Erede
#Assumete che il proprietario dell’oggetto sia l’antenato che compare la prima volta (dall’inizio del file) 
#assieme all’oggetto e che se l’antenato NON ha l’oggetto allora l’erede NON lo riceve. Assumete inoltre 
#che l’ordine delle righe conti: in una riga, l’antenato A possiede un oggetto solo se A è il proprietario, 
#oppure se esiste una riga precedente in cui A riceve l’oggetto da un antenato che ha l’oggetto.
#La funzione deve leggere il file e restituire il dizionario con chiavi i nomi degli oggetti nel file e come 
#valore associato a ciascuna chiave k una lista contenente due nomi, il nome del proprietario e il nome 
#dell’ultimo erede che ha ricevuto l’oggetto k. Ad esempio se il file contiene: 
#Oggetto,Antenato,Erede
#Anello_di_smeraldi,Maria,Paola
#Anello,Silvia,Paolo
#Anello_di_smeraldi,Paola,Anna
#Anello_di_smeraldi,Anna,Giorgia
#la funzione deve restituire: 
#{'Anello_di_smeraldi': ['Maria','Giorgia'], 'Anello': ['Silvia', 
#'Paolo']}
import re
def Ex4(file):
    fin=open(file,encoding='utf-8')
    lista=[]
    d={}
    for elem in fin:
        lista.append(elem.strip().split(','))
    if len(lista)!=0:
        lista.remove(lista[0])
    for parola in lista:
        if parola[0] not in d:
            d[parola[0]]=[]
            d[parola[0]].append(parola[1])
            d[parola[0]].append(parola[2])
        elif (d[parola[0]][1])==parola[1]:
            d[parola[0]].remove(parola[1])
            d[parola[0]].append(parola[2])
    return d
    
    
            
            
        
            
        #posso mettere l'oggetto in un insieme o lista. se già c'è, allora posso capire se l'antenato è nuovo o è il primissimo possessore dell'oggetto
        
    
        #devo riconoscere la combinazione di caratteri all'ultima riga con RE
    
    
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""
    
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
