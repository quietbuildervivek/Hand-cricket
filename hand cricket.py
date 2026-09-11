# hand cricket game bana jisme runs max 6 bana sake and hand cricket ke rules same rakhna 
import random
RUN=[1,2,3,4,5,6]

total_runs=0
#this is for batting part of hand cricket game where user will input the runs and computer will 
# randomly choose the runs and if both are same then user is out otherwise total runs will be added
runs=int(input("swing the bat: "))
# thinking how a user can only input runs from 1 to 6 and if user inputs more than 6 then it should show invalid input and ask for input again
# thinking of a way how to make the game more interesting by adding a bowling part where computer will bat and user will bowl
for i in range(1,7):# this is working as number of balls in hand cricket game
    comp=random.choice(RUN)
    print("computer chose: ",comp) # this is for checking what computer has chosen and to check if user is out or not
    if runs==comp:
        print("you are out")
        break
    else:
        total_runs+=runs
        print("TOTAL: ",total_runs)
        runs=int(input("swing the bat: "))
        
   