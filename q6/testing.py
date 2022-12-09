line=["k","l","k","k","m","n","o","p","q"]
tester=[]
seen=[]
found=False
foundPlace=0

for i in range(len(line)):
    print("i Right Now: ",i)
    if i<=3:
        tester.append(line[i])
    else:
        print("Test Array Before: ",tester)
        for char in tester:
            # print("CHar RN: ",char)
            if char in seen:
                print("CHar popped: ",char)
                tester.pop(0)
                break
            else:
                seen.append(char)

                if len(seen)==4:
                    foundPlace=i
                    print("Found it at place: ",foundPlace)
                    found=True

        tester.append(line[i]) # Adding new character
        print("Seen Array: ",seen)
    
    if found==True:
        break

    seen.clear()
    print("Test Array After: ",tester)
    print("Seen Array After: ",seen)