
class numbers:
    a = 33
    b = 55
    c = 44

p1 = numbers()
# Relational Operators includes Greater than (<), Less than (>), equals to (==), not equals to (!=), it just gives you True or False
print ("Relational Operations:")
print ("'a' is greater than 'b':",p1.a>p1.b)
print ("'a+b' is less than 'c':",p1.a+p1.b<p1.c)
print ("'a+c' is equals to 'b':",p1.a+p1.c==p1.b)
print ("'a+c' is not equals to 'b':",p1.a+p1.c!=p1.b)

# Arithmetics Operators includes addition (+), subtraction (-), division (/), Multipilication (*)
print ("Arithmatic Operations:")
print ("adiition & subtraction of variables (a+b-c) gives you",p1.a+p1.b-p1.c)
print ("Multiplication & divisions of varibales (a*b/c) gives you",p1.a*p1.b/p1.c)


"""Logical Operators includes 
Both operants equal (&), if 1 statement of them is false it gives you false, if both statements are true it gives you true
Both operants aren't equal (|),if 1 statement of them is false it gives you True, if both statements are true it gives you False"""

class statement:
    a = True
    b = False

p2 = statement()
print ("Logical Operations:")
print ("'a' and 'b' is equal :",p2.a&p2.b)
print ("'a' and 'b' is not equal :",p2.a|p2.b)