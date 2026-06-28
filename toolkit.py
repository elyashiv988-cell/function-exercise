# part 1
# 1
def greet(name):
    print("hello",name)
greet("agent x")
# 2
def add(a,b):
    print(a+b)
add(3,4)
# 3
def square(n):
    print(n**2)
square(5)
square(12)
# 4
def greet_with_title(name, title="Agent"):
    print("hello",title,name)
greet_with_title(name="eli")
greet_with_title("eli","student")
# 5
def describe(name, level, active):
    print("name: ",name)
    print("level: ",level)
    print("active",active)
describe("eli",10,True)
