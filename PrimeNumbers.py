primenumbers=[]
intnum = int(input("请输入一个整数: "))
print("1-"+str(intnum)+"范围内的素数有：\n")
for num in range(2, intnum) :
    for i in range(2, num) :
        if num % i == 0 :
            break
    else :
        primenumbers.append(num)
    dict1={}
    d

print(primenumbers)