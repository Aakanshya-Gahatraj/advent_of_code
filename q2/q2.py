# 1st Question -------------------

# Rock defeats Scissors, Scissors defeats Paper, and Paper defeats Rock

# opponent is going to play: A for Rock, B for Paper, and C for Scissors.
# my response: X for Rock, Y for Paper, and Z for Scissors.

# Strategy to win:
# A Y
# B Z
# C X

# Score
# Rock= 1 point, Paper= 2 points, Scissors= 3 points
# lost= 0 point, draw= 3 points, won= 6 points

# Ans (myFirstQuesPoints): 11906

# 2nd Question [Rule changed] ---------------------

# X= you need to lose, 
# Y= you need a draw,
# Z= you need to win.

# Ans (mySecQuesPoints): 

f= open("q2/q2_file.txt","r")
line=[]
myFirstQuesPoints=0
mySecQuesPoints=0

for x in f:
    line= x.strip() # removes whitespace, new line
    if (line[0]== "A" ): # opp throws rock
        if(line[2]=="X"): # i throw rock (1 pt) or as per ques:2, i need to lose (0 pt)
            myFirstQuesPoints+= 1+3 # draw (3 pt)
            mySecQuesPoints+= 3+0 # i throw scissors (3 pt)
        elif(line[2]=="Y"): # i throw paper (2 pt) or as per ques:2, i need a draw (3 pt)
            myFirstQuesPoints+= 2+6 # i win (6 pt)
            mySecQuesPoints+= 1+3 # i throw rock (1 pt)
        elif(line[2]=="Z"): # i throw scizzors (3 pt) or as per ques:2, i need to win (6 pt)
            myFirstQuesPoints+= 3+0 # i lose (0 pt)
            mySecQuesPoints+= 2+6 # i throw paper (2 pt)
    
    if (line[0]== "B"): # opp throws paper
        if(line[2]=="X"): # i throw rock or need to lose
            myFirstQuesPoints+= 1+0 # i lose
            mySecQuesPoints+= 1+0 # i throw rock
        if(line[2]=="Y"): # i throw paper or need a draw
            myFirstQuesPoints+= 2+3 # draw
            mySecQuesPoints+= 2+3 # throw paper
        if(line[2]=="Z"): # i throw scizzors or need a win
            myFirstQuesPoints+= 3+6 # i won
            mySecQuesPoints+= 3+6 # i throw scizzors

    if (line[0]== "C"): # opp throws scizzors
        if(line[2]=="X"): # i throw rock or need to lose
            myFirstQuesPoints+= 1+6 # i won
            mySecQuesPoints+= 2+0 # i throw paper
        if(line[2]=="Y"): # i throw paper or need a draw
            myFirstQuesPoints+= 2+0 # i lose
            mySecQuesPoints+= 3+3 # i throw scizzors
        if(line[2]=="Z"): # i throw scizzors or need to win
            myFirstQuesPoints+= 3+3 # draw
            mySecQuesPoints+= 1+6 # i throw rock

print(myFirstQuesPoints)
print(mySecQuesPoints)



