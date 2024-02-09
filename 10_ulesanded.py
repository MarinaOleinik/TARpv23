#15
for j in range(0,105,5):
    for i in range(0,105,5):
        print(f"{i*j:5}",end=" ")
    print()
#1
#for
r=0
for i in range(15):
    arv=float(input("Sisesta {0}.arv ".format(i+1)))
    if arv==int(arv):
        r+=1
print("Täisarvude arv on "+str(r))
#while True
r=0
i=0
while True:
    i+=1
    arv=float(input("Sisesta {0}.arv ".format(i)))
    if arv==int(arv):
        r+=1
    if i==15: break
print("Täisarvude arv on "+str(r))    
#while tingimustega
r=0
i=0
while i<15:
    i+=1
    arv=float(input("Sisesta {0}.arv ".format(i)))
    if arv==int(arv):
        r+=1

print("Täisarvude arv on "+str(r))  
