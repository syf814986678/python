import random
a=0
i=0
def gowhere(i):
    mylist=["西安","长沙","重庆","哈尔滨","泰国"]
    print(mylist[i])
while(i<10):
    a=random.randint(0,4)
    i+=1
    print(a)
gowhere(a)