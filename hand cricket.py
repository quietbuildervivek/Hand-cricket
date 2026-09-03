# hand cricket game bana jisme runs max 6 bana sake and hand cricket ke rules same rakhna 
import random
RUN=[1,2,3,4,5,6]
comp=random.choice(RUN)
total_runs=0
#this is for batting part of hand cricket game where user will input the runs and computer will 
# randomly choose the runs and if both are same then user is out otherwise total runs will be added
runs=int(input("swing the bat: "))
for i in range(1,7):# this is working as number of balls in hand cricket game
    if runs==comp:
        print("you are out")
        break
    else:
        total_runs+=runs
        print("your total runs are: ",total_runs)
        runs=int(input("swing the bat: "))
        
           