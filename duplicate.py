dic={
    "ball":"red",
    "bat":4,
    "wicket":8,
    "ball":"green",
    "bat":3,
    "wicket":3
    } 
result = {}
for key in dic:
    for i in dic:
        if key==i:
            result.get(key)
            del i
            print(dic)
        break
