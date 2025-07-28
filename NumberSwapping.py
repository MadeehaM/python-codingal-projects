x=int(input("x="))
print("The value of x is ",x)

y=int(input("y="))
print("The value of y is ",y)

z=int(input("z="))
print("The value of z is ",z)

numbers=[x, y, z]
numbers.sort()

opp=[x,y,z]
opp.sort(reverse=True)

print("Numbers in ascending order:",numbers )
print("Numbers in descending order:", opp)

