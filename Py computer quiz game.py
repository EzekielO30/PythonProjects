print("Welcome to my life quiz!!")

playing = input ("Do you want to play? \n")

if playing.lower() != "yes": 
    quit()

print ("Okay! Let's play and goodluck :)")
score =  0

answer = input("What does Mofiyinfoluwa stand for? ")
if answer.lower()  == "i give all the glory to god":
    print ("Correct!")
    score += 1
else: 
    print(" INcorrrect.")    

answer = input("How many siblings does Ezekiel have?(L format) ")
if answer.lower() == "3":
    score += 1
    print ("Correct!")
else: 
    print(" INcorrrect.")    

answer = input("What is Ezekiel's Birthday?(N Format) ")
if answer.lower() == "08/30":
    print ("Correct!")
    score += 1
else: 
    print(" INcorrrect.")    

answer = input("How many times does fiyin cry?(L format) ")
if answer.lower()  == "zero":
    print ("Correct!")
    score += 1
else: 
    print(" INcorrrect.")    
    
print("You got " + str (score) + " questions correct!")   
print("You got " + str((score/4) * 100) + " %.")
