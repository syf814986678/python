import random
while (1):
    roundnum=0
    end=0
    guessnum=random.randint(0,10)
    # print(guessnum)
    while(end==0):
        num=int(input("请输入您预测的数\n"))
        if(num<guessnum):
            print("遗憾，太小了\n")
            roundnum+=1
            continue
        elif(num>guessnum):
            print("遗憾，太大了\n")
            roundnum+=1
            continue
        end=1
    print("预测"+str(roundnum)+"次，你猜中了！\n")





            
