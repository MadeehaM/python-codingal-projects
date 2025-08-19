FirstFile= open('file.txt', 'r')
print("Read mode:")
print(FirstFile.read())
FirstFile.close()

Second = open('file.txt', 'w')
Second.write("Write mode: \n")
Second.write("Testing")
Second.close()

Third = open('white.txt', 'a')
Third.write("Append mode: \n")
Third.write("This is a test \n")
Third.close()