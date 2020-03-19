dict1={}
while (1):
    name=input("请输入姓名(输入exit退出)")
    if(name!="exit"):
        tel=input("请输入电话")
        dict1[name]=tel
        continue
    break
# print(dict1)     
for name in dict1.keys():
    print(str(name)+"："+str(dict1[name]))  

name=input("查询姓名")
if(name in dict1):
    print(str(name)+"："+str(dict1[name]))
else:
    print("不存在此用户")
