#User se 10 students ke naam aur marks lekar unhe ek dictionary me store karaye.


data={}
i=0
while i<4:
    (name , marks)=input("name:-"), int(input("marks:-"))
    # marks=int(input("marks:-"))
    data[name]=marks
    i=i+1
print(data)



# name=['sonu','kartik','Deepak','Aman','Somesh','Umesh','Amarpal','Roshan','Riyaj','Shabib']
# marks=[90,96,76,60,85,70,57,98,56]
# dic={}
# for key in name:
#     for value in marks:
#         dic[key]=value
#         marks.remove(value)
#         break
# print(dic)


