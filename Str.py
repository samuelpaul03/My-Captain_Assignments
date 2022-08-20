s = input ("Enter the word :- ")
c = input ("Enter the character :- ")
str = ""
for i in range (len (s)) :
    if s[ i ] == c :
        str += s[ i ].upper()
    else :
        str += s[ i ]
print (str)