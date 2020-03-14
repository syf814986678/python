import random
while (1):
    roundnum=1
    end=0
    guessnum=random.randint(0,9)
    # print(guessnum)
    while(1):
        num=int(input("请输入您预测的数\n"))
        if(num<guessnum):
            print("遗憾，太小了\n")
            roundnum+=1
            continue
        elif(num>guessnum):
            print("遗憾，太大了\n")
            roundnum+=1
            continue
        break
    print("预测"+str(roundnum)+"次，你猜中了！\n")





            
