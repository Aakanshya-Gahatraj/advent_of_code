# Question 2-----------------------

f= open("q3/q3_file.txt","r")
allLines= f.readlines()
# print(len(allLines)) # 300 lines
sumOfPriorityIn3=0

for i in range(0,len(allLines),3):
    newline= allLines[i].strip()
    # print(newline)
    for char in newline:
        if(char in allLines[i+1] and char in allLines[i+2]):
            sameCharIn3=char 
    # print(sameCharIn3)

    if sameCharIn3>= "a" and sameCharIn3<= "z":
        charPriority= ord(sameCharIn3)- ord("a") +1
        sumOfPriorityIn3+=charPriority
    
    elif sameCharIn3>= "A" and sameCharIn3<= "Z":
        charPriority= ord(sameCharIn3)- ord("A") +27
        sumOfPriorityIn3+=charPriority

print(sumOfPriorityIn3)