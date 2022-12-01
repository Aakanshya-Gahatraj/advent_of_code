f= open("q1/q1_file.txt","r")
elves=[]
sum=0
for x in f:
    if x.strip()=="":   #checks if line is new line 
        elves.append(sum)
        # print("here, {i}")
        sum=0
    else:
        sum+= int(x)
        # print(sum)
    
print(max(elves))
elves.sort(reverse=True)
# print(elves)
print(elves[0]+elves[1]+elves[2])

    
