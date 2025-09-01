Fn1 = open('text1.txt', 'r')
print(Fn1.read())
Fn1.close()

Fn2 = open('text1.txt', 'r')
print("\n First 10 characters: \n")
print(Fn2.read(10))
Fn2.close()

Fn3 = open('text1.txt', 'r')
print("First Line:")
print(Fn3.readlines())
Fn3.close()

Fn4 = open('text1.txt', 'r')
print("First four Line:")
print(Fn4.readlines())
print(Fn4.readlines())
print(Fn4.readlines())
print(Fn4.readlines())
Fn4.close()

Fn5 = open('text1.txt', 'r')
print("Looping through content:")
for lines in Fn5:
    print(lines)
Fn5.close()