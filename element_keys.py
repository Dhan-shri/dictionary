#Do lists lekar ek dictionary banaiye jisme pehli list ke elements keys 
# ho aur dusri list ke elements unn keys ki values ho. 
list1=["one","two","three","four","five"]

list2=[1,2,3,4,5,]  
d={}
for key in list1:
    for value in list2:
        d[key]=value
        list2.remove(value)
        break
print(d)
