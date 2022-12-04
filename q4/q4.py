f=open("q4/q4_file.txt","r")
a=[]
b=[]
aBegin=[]
aEnd=[]
bBegin=[]
bEnd=[]
q1count=0
q2count=0

for x in f:
    line= x.strip()
    a.append(line.split(",")[0])
    b.append(line.split(",")[1])

# print(len(a))

for i in range(len(a)):
    aBegin.append(int(a[i].split("-")[0]))
    aEnd.append(int(a[i].split("-")[1]))
    bBegin.append(int(b[i].split("-")[0]))
    bEnd.append(int(b[i].split("-")[1]))

    if((aBegin[i]<=bBegin[i] and aEnd[i]>=bEnd[i]) or (bBegin[i]<=aBegin[i] and bEnd[i]>=aEnd[i])): # completely enclosed
        q1count+=1
        # print(aBegin[i],"-",aEnd[i],"  ",bBegin[i],"-",bEnd[i]," ",count)
        q2count+=1
    elif((aBegin[i]<=bBegin[i] and bBegin[i]<=aEnd[i]) or (bBegin[i]<=aBegin[i] and aBegin[i]<=bEnd[i])):
        q2count+=1

print(q1count)
print(q2count)



