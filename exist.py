#Ek program likhiye jisse ki agar di hui 
# key pehle se dictionary me exist karti ho toh “exists “ print kare aur agar nahi karti ho toh “not exists” print kare.
dict={"name":"Raju", "marks":56}
key=input("enter a key")
if key in dict:
    print("exist")
else:
    print("not exist")