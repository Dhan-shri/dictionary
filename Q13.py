my_dict = {
    'a':50, 
    'b':58,
    'c': 56,
    'd':40,
    'e':100, 
    'f':20
    } 

# expect result:-['e','b','c']
# k={}
# l={}
# for x,y in my_dict.items():
#     k.update({y:x})
# print(k)
# p=[]
# for keys in k:
#     p.append(keys) 
# p.sort()
# x=(p[-3:])
# # print(x)
# print()


# f_max=0
# s_max=0
# t_max=0
# k={}
# for i in my_dict:
#     if (f_max<my_dict[i]):
#         f_max=my_dict[i]
#     for j in my_dict:
#         if (s_max<my_dict[j]) and (f_max>my_dict[j]):
#             s_max=my_dict[j]
#     for k in my_dict:
#         if f_max>my_dict[k] and s_max>my_dict[k] and t_max<my_dict[k]:
#             t_max=my_dict[k]
# k["f_max"]=f_max
# k["s_max"]=s_max
# k["t_max"]=t_max
# print(k)        



