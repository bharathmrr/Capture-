
l=['a','b','c','d','e','f','g','#','@','&','*']
cap=[]
enter=[]
import random as r
for i in range(6):
    w=r.choice(l)
    cap.append(w)
print("enter the below cap")
for i in cap:
    print(i,end="")
print()
c=input("")
for i in c:
    enter.append(i)

if enter==cap:
    print("login proceed")
else:
    print("not proceed")
