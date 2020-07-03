pos=[]
InputList=list(map(int,input("Enter input list with spaces in between each number").split()))
for i in InputList:
    if i>0:
        pos.append(i)
print("The positive number are ",pos)
