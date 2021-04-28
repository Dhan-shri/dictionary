lst=[
     {"first":"1"}, 
     {"second": "2"}, 
     {"third": "1"}, 
     {"four": "5"}, 
     {"five":"5"}, 
     {"six":"9"},
     {"seven":"7"}
]

# [2', '7', '9', '5', '1'] 
dict1={}
i=0
while i<len(lst):
     num=lst[i]
     dict1.update(num)
     i=i+1
# print(dict1)
k=[]
for x in dict1.values():
     k.append(x)
# print(k)
t=[]
for a in k:
     if a not in t:
          t.append(a)
for a in t:
     print(t)
     break







 

