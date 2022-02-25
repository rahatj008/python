# List are the elements which are enclosed with [], there are mutable means it can be changed

a = [44, "renew", 9.33, True, False]
print (a)
# output : [44, 'renew', 9.33, True, False]
print (type(a))
# output : <class 'list'>

# extracting individual
print (a[0:2])
# output : [44, 'renew']

# replacing index value in list
a[0] = 22
print (a)
# output : [22, 'renew', 9.33, True, False]

# adding a new value in the list
a.append("rahat")
print (a)
# output : [22, 'renew', 9.33, True, False, 'rahat']

# removing the element in the list
a.pop(0)
print (a)
# outptut : ['renew', 9.33, True, False, 'rahat']

# Reversing index orders for whole string
a.reverse()
print (a)
# output : ['rahat', False, True, 9.33, 'renew']

# Inserting elements at specific index 
a.insert (2, "ramp")
print (a)
# output : ['rahat', False, 'ramp', True, 9.33, 'renew']

# sorting a list, it can arrange values with alphabetic order
b = ["rahat", "badar", "noman", "bilal", "ahad"]
b.sort()
print (b)
# output : ['ahad', 'badar', 'bilal', 'noman', 'rahat']

# Repeating & Concatenating in list, same procedure as variables & Tuples
print (a*2+b*3)
# output : ['rahat', False, 'ramp', True, 9.33, 'renew', 'rahat', False, 'ramp', True, 9.33, 'renew', 'ahad', 'badar', 'bilal', 'noman', 'rahat', 'ahad', 'badar', 'bilal', 'noman', 'rahat', 'ahad', 'badar', 'bilal', 'noman', 'rahat']
