my_dict = {
    'a':50, 
    'b':777, 
    'c':231,
    'd':40, 
    'e':100, 
    'f':20,
    'g':98,
    'h':320,
    'r':345,
    't':12
    }
k=[]
for x in my_dict.values():
    k.append(x)
i=0
while i<len(k):
    j=0
    while j<len(k)-1:
        if k[j]>k[j+1]:
            k[j],k[j+1]= k[j+1],k[j]
        j=j+1
    i=i+1
print(k)
a=k[-3:]
print(a)

# my_dict = {
#     'a':50, 
#     'b':58, 
#     'c':231,
#     'd':40, 
#     'e':100, 
#     'f':20,
#     'g':98,
#     'h':320
#     }
# k=[]
# for x in my_dict.values():
#     k.append(x)
# i=0
# s=[]
# n=k[0]
# while i<len(k):
#     num=k[i]
#     if num>n:
#         n=num
#     i=i+1
# s.append(n)
# k.remove(n)
# j=0
# a=k[0]
# while j<len(k):
#     b=k[j]
#     if b>a:
#         a=b
#     j=j+1
# s.append(a)
# k.remove(a)
# u=0
# a=k[0]
# while u<len(k):
#     b=k[u]
#     if b>a:
#         a=b
#     u=u+1
# s.append(a)
# # k.remove(a)
# print(s)



