n = int(input("Inserire un numero n: "))

#Verifica numero primo
Primo = False

i = 2

count = 0

while i < n:
    if n % i != 0:
        count = count + 1
    i = i + 1

if count + 2 == n:
    Primo = True


#Codice Print (es. 10)

if Primo:
	p = 2
	count = 0
	i = 1
	while p <= n:
     		while i <= p:
     			if p % i != 0:
     				count = count + 1
     			i = i + 1
     			
     		if count + 2 == p:
     		 	print(p)
     		count = 0
     		i = 1
     		p = p + 1
else:
	p = 2
	count = 0
	i = 1
	while p < n:
     		while i <= p:
     			if p % i != 0:
     				count = count + 1
     			i = i + 1
     			
     		if count + 2 == p:
     		 	print(p)
     		count = 0
     		i = 1
     		p = p + 1