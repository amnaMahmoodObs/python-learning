print ("hello world!")
a = [1, 2, 3]
b = a
a +=[4, 5]
print(b)

c = "hello world, i am trying to learn pythonfdkfjjdkfjdkljfdkljfdkljfkldjfkdjfjd"
d = c
print(c is d)

def modify(x):
    x.append(4)
    x = [1,2,3]
    return x

lst = [0]
modify(lst)
print(lst)
print("*"*10)
def func():
    try:
        return "A"
    finally:
        return "C"

print(func())

for _ in range (10):
    print(_)