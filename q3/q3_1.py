#  a through z have priorities 1 through 26.
#  A through Z have priorities 27 through 52.

# Question 1----------------------

f= open("q3/q3_file.txt","r")
sumOfPriority=0

for x in f:
    line= x.strip()

    length=len(line)
    divider= int(length/2)
    firstHalf=line[:divider]
    secHalf=line[divider:]

    for char in firstHalf:
        if(char in secHalf):
            # print(char) # found the same character
            sameChar=char 
    
    if sameChar>= "a" and sameChar<= "z":
        # print(sameChar, ord(sameChar))
        charPriority= ord(sameChar)- ord("a") +1
        # print(sameChar," ", charPriority) # Priority found
        sumOfPriority+=charPriority
    
    elif sameChar>= "A" and sameChar<= "Z":
        # print(sameChar, ord(sameChar))
        charPriority= ord(sameChar)- ord("A") +27
        # print(sameChar," ", charPriority) # Priority found
        sumOfPriority+=charPriority

print(sumOfPriority)

