def calweight(weight,year):
    weight+=0.5*year
    return weight
while(1):
    weight=int(input("请输入体重\n"))
    year=int(input("请输入时间\n"))
    print("地球上"+str(year)+"年后为"+str(calweight(weight,year))+"KG\n")
    print("月球上"+str(year)+"年后为"+str(calweight(weight,year)*0.165)+"KG\n")