# Set is an unordered & unindexed data structure in Python, it uses {}, we cannot take out things by indexes
# Duplicates aren't allowed
# Set & Dictionary has differnces, dictionary has key-value pair, but set has unordered data
a = {2, "rahat", "rahat", True, True, 2, 4}
b = {3, 4, "rahat", False, True}
print (a)
# output : {True, 2, 4, 'rahat'}

# adding a single element & adding a multiple element
a.add("renew")
print (a)
# output : {True, 2, 4, 'renew', 'rahat'}

a.update(["eminem", "lady gaga", "pitbull"])
print (a)
# output : {True, 2, 4, 'pitbull', 'renew', 'eminem', 'lady gaga', 'rahat'}

# removing an element
a.remove("renew")
print (a)
# output : {True, 2, 4, 'lady gaga', 'pitbull', 'rahat', 'eminem'}

# Union & Intersection operations can be easily done on sets
print (a.union(b))
