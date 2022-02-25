# Dictionary is an unordered pair of key-value collection, it uses {}, Dictionary is mutable
# like a = {"orange":3}, here "orange" is the key and "3" is the value here
a = {"rahat":24, "waqar":30, "arsalan":33}
print (a)
# ouput : {'rahat': 24, 'waqar': 30, 'arsalan': 33}
print (type(a))
# output : <class 'dict'>

# printing full item
print (a.items())
# output : dict_items([('rahat', 24), ('waqar', 30), ('arsalan', 33)])

# Extracting keys & Values in dictionary
print (a.keys(), a.values())
# output : dict_keys(['rahat', 'waqar', 'arsalan']) dict_values([24, 30, 33])

# Adding a new element in dictionary
a["Faraz"]=26
print (a)
# output : {'rahat': 24, 'waqar': 30, 'arsalan': 33, 'Faraz': 26}

# changes in existing value 
a["Faraz"]=27
print (a) 
# output : {'rahat': 24, 'waqar': 30, 'arsalan': 33, 'Faraz': 27}

# Adding 1 dictionary to another dictionary
b = {"zunair":29, "hussain":36, "musharib":31}
a.update(b)
print (a) 
# output : {'rahat': 24, 'waqar': 30, 'arsalan': 33, 'Faraz': 27, 'zunair': 29, 'hussain': 36, 'musharib': 31}

# removing (popping) an element
a.pop("rahat")
print (a)
# output : {'waqar': 30, 'arsalan': 33, 'Faraz': 27, 'zunair': 29, 'hussain': 36, 'musharib': 31}


 