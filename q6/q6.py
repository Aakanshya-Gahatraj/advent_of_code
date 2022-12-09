
f= open("q6/q6_file.txt")
line=[]

while True:
    char = f.read(1) # reading per char
    line.append(char)
    if not char:
        print('Reached end of file')
        break

def finder (line, limit):
    tester=[]
    seen=[]
    found=False
    foundPlace=0

    for i in range(len(line)):
        # print("i Right Now: ",i)
        if i<=(limit-1):
            tester.append(line[i])
        else:
            # print("Test Array Before: ",tester)
            for char in tester:
                if char in seen:
                    # print("CHar popped: ",char)
                    tester.pop(0)
                    break
                else:
                    seen.append(char)

                    if len(seen)==limit:
                        foundPlace=i
                        # print("Found it at place: ",foundPlace)
                        found=True

            tester.append(line[i]) # Adding new character
            # print("Seen Array: ",seen)

        seen.clear()
        # print("Test Array After: ",tester)
        # print("Seen Array After: ",seen)
        
        if found==True:
            return foundPlace

q1Ans=finder(line,4)
q2Ans=finder(line,14)
print("Q1 Found: ",q1Ans)
print("Q2 Found: ",q2Ans)
