word1 = input("insert word: ")
word2 = input("insert word: ")
number = int(input("Insert number: "))
finalLetter=''
for counter in range(0, len(word1)):
    if word1[counter] in word2:
        lettera = word2.find(word1[counter])
        if (abs((lettera - counter)) <= number or abs((counter - lettera)) <= number):
            finalLetter+=(word1[counter])
print(finalLetter)