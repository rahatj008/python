# Tuples are enclosed in (), 
new = ("noman", 2, False, True, "P", "daniyal")
new1 = (24, True, "Contractual")
print (new)
# output : ('noman', 2, False, True, 'P', 'daniyal')
print (type(new))
# output : <class 'tuple'>

# extracting individual substring are similar as variables in tuple, but it can print full string mentioned, instead of each word
print (new[-1])
# output : daniyal

print (new[2:4])
# output : (False, True)

# extracting length of tuple.
print (len(new))
# output : 6

# Concatenating the tuple, it could help in joining 2 sentence without muting anything
print (new+new1)  
# output : ('noman', 2, False, True, 'P', 'daniyal', 24, True, 'Contractual')

# Repeating tuples
print (new*2)
# output : ('noman', 2, False, True, 'P', 'daniyal', 'noman', 2, False, True, 'P', 'daniyal')

print (new*3+new1*2)
# output : ('noman', 2, False, True, 'P', 'daniyal', 'noman', 2, False, True, 'P', 'daniyal', 'noman', 2, False, True, 'P', 'daniyal', 24, True, 'Contractual', 24, True, 'Contractual')

# Extracting minimum & maximum values from tuples, but your tuple has integer value 
a = (9,4,2,6,7,5)
print (min(a), max(a))
# output : 2 9
