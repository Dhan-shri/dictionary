dic={'bijender':4,'deepak':60,'param':20,'anjili':30,'roshini':50}
k={}
for i in dic:
    a=dic[i]
    for j in dic:
        b=dic[j]
        if a>b:
            k[j]=b
for i in dic:
    a=dic[i]
    for j in dic:
        b=dic[j]
        if a<b:
            k[j]=b
print(k)
# l={}
# for i in dic:
#     a=dic[i]
#     for j in dic:
#         b=dic[j]
#         if a<b:
#             l[j]=b
# for i in dic:
#     a=dic[i]
#     for j in dic:
#         b=dic[j]
#         if a>b:
#             l[j]=b
# print(l)

dic={'bijender':4,'deepak':60,'param':20,'anjili':30,'roshini':50}
k={}
l=len(dic)
print(l)
for i in range(l):
    max_1=0
    for value in dic:
        if max_1 <dic[value]:
            max_1=dic[value]
            key=value
    k.update({key:max_1})
    dic.pop(key)
print(k)


