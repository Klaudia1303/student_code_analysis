s_1 = input('stringa 1 = ')
s_2 = input('stringa 2 = ')
i = 0

while len(s_1) != len(s_2):
    s_1 = input('stringa 1 = ')
    s_2 = input('stringa 2 = ')

for i in range(len(s_1)):
    print(s_1[i]+s_2[i], end='')
    i = i +1
    
