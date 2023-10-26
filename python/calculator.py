x = int(input("enter first input"))
y = int(input("enter second input"))

def add(x, y):
    print(x, "+", y, "=", x + y)
def sub(x, y):
    print(x, "-", y, "=", x - y) 
def mul(x, y):
    print(x, "*", y, "=", x * y)
def div(x, y):
    print(x, "/", y, "=", x / y)

operation = input("what is the opertion?")

if operation == "add":
  add(x, y)
if operation == "sub":
  sub(x, y)
if operation == "mul":
  mul(x, y)
if operation == "div":
  div(x, y)

error =  ZeroDivisionError

if operation == "div" and y == 0 :
   print(error)
 
def exit() :
   quit

answer = input("do you want to exit")

if answer == "yes":
   exit()
