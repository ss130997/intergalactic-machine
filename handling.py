
try:
    f = open("ab.txt")
    for line in f:
        print(line)
except:

    print("You have to create the file first")

try:
    r = open("ab.txt")
except FileNotFoundError:
    print("File Not Found")

try:
    a = 10/0
    l = [1, 2, 3]
except(ZeroDivisionError, IndexError):
    print("Try to handle error")

try:
    a = open("ab.txt")
    for line in a:
        print(line)
except Exception as e:
    print(e.filename)

try:
    z =10/0
except Exception as e:
    print(type(e))

#We added it here just for fun
