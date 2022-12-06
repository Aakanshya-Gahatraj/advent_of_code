# Question 2 ----------------------------
f=open("q5/q5_file.txt","r")
lines=f.readlines()
stack=[]
commands=[]
limit=0

# print(len(lines))
for i in range(len(lines)):
    if lines[i+1]=="\n":
        break
    else:
        stack.append(lines[i])
        limit+=1

# print(cnt)
for i in range(limit+2,len(lines)):
    commands.append(lines[i].strip())

# print(stack)
# print(commands)

finalList=[]
cnt=0

for i in range(len(stack)):
    for j in range(len(stack[i])):
        if stack[i][j]==" ":
            cnt+=1
            # print(cnt)
        elif stack[i][j]=="[" or stack[i][j]=="]" or stack[i][j]=="\n":
            if cnt!=0:
                if cnt>=4 and cnt<8:
                    # print("less cnt",cnt)
                    finalList.append("0")
                elif cnt>=8:
                    # print("more cnt",cnt)
                    finalList.append("0")
                    finalList.append("0")
            cnt=0
            continue
        else:
            finalList.append(stack[i][j])
# print(finalList)

a1=[]
a2=[]
a3=[]
a4=[]
a5=[]
a6=[]
a7=[]
a8=[]
a9=[]

for i in range(0,len(finalList),9):        
    a1.append(finalList[i])
    a2.append(finalList[i+1])
    a3.append(finalList[i+2])
    a4.append(finalList[i+3])
    a5.append(finalList[i+4])
    a6.append(finalList[i+5])
    a7.append(finalList[i+6])
    a8.append(finalList[i+7])
    a9.append(finalList[i+8])
    
a1.reverse()
a2.reverse()
a3.reverse()
a4.reverse()
a5.reverse()
a6.reverse()
a7.reverse()
a8.reverse()
a9.reverse()

# for i in range(len(a1)):

def remove0(a):
    return list(filter(("0").__ne__, a))

a1=remove0(a1)
a2 = remove0(a2)
a3 = remove0(a3)
a4 = remove0(a4)
a5 = remove0(a5)
a6 = remove0(a6)
a7 = remove0(a7)
a8 = remove0(a8)
a9 = remove0(a9)
 
# print(a1)
# print(a2)
# print(a3)
# print(a4)
# print(a5)
# print(a6)
# print(a7)
# print(a8)
# print(a9)

dict={1:a1,2:a2,3:a3,4:a4,5:a5,6:a6,7:a7,8:a8,9:a9}

temp=[]
def shiftAsCommand2(dict):
    for i in range(len(commands)):
        commandsNum = [int(i) for i in commands[i].split() if i.isdigit()]
        if commandsNum[0]==1:
            move= dict[commandsNum[1]].pop()
            dict[commandsNum[2]].append(move)
        else:
            for i in range(commandsNum[0]):
                temp.append(dict[commandsNum[1]].pop())
            for i in range(commandsNum[0]):
                dict[commandsNum[2]].append(temp.pop())

shiftAsCommand2(dict)

topWords=""
for i in range(1,10):
    topWords= topWords+dict[i][-1]

print("Q2: ",topWords)