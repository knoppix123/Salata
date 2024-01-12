import random
def test1():
    print("test1")

def test2():
    print("test2")

list = [test1, test2]
listselect = random.choice(list)

listselect()