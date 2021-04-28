# word="MISSISSIPPI"
# i=0
# dic={}
# count=0
# b=word[0]
# while i<len(word):
#     a=word[i]
    
    
word="MISSISSIPPI"
k=[]
x={}
for i in word:
    k.append(i)
    s=k.count(i)
    x.update({i:s})
print(x)


    

    
