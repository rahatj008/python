# Strings are the data type in Python
# strings are the character which uses (''),(""),(""")
# Extracting individual characters by index value. type "variable[desired-index-value]" to get word as per your desire
# spaces are also counted as index values
ilma = "Rahat is the student of ilma university"
print (type(ilma))
# output : <class 'str'> 

print (ilma[0],ilma[1],ilma[-1],ilma[6])
# Output : R a y i
print (ilma[0:5], ilma[29:39])
# Output : Rahat university

# To find the length of string in python, type "len(variable)"
print (len(ilma))
# Output : 39

# To convert string to lower case, type variable.lower()
print (ilma.lower())
#output : rahat is the student of ilma university

# To convert string to lower upper, type variable.upper()
print (ilma.upper())
#output : RAHAT IS THE STUDENT OF ILMA UNIVERSITY

# Replacing a sub string, type "variable.replace('new_substring', 'old_substring')"
print (ilma.replace('a','b'))
#output : Rbhbt is the student of ilmb university

#Find a number of occurences of sub string, type "variable.count("sub-string")"
alpha = "rock and roll, rock and roll"
print (alpha.count("rock"))
#output : 2

#Find index of sub string, it gives you the starting index number of sub-string
print (ilma.find("Rahat"))
# output : 0

# Spliting a string by using 1 constant, in-between string
beta = "rahat has 3 things_ skills_ knowledge_ expertise"
print (beta.split('_'))
# output : ['rahat has 3 things', ' skills', ' knowledge', ' expertise']

# repeating variables
print (beta*2)
# output : rahat has 3 things_ skills_ knowledge_ expertiserahat has 3 things_ skills_ knowledge_ expertise

# concatenating variables
print (alpha+beta)
# output : rock and roll, rock and rollrahat has 3 things_ skills_ knowledge_ expertise


