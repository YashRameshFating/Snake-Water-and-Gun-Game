import random
'''
Snake Water Gun Game
1 for snake
-1 for water 
0 for gun

'''
computer=random.choice([1,0,-1])
yourstring=input("Enter your choice (snake, water, gun): ").lower()
yourDict={"snake":1,"water":-1,"gun":0}
reverseDict={1:"snake",-1:"water",0:"gun"}
your=yourDict[yourstring]
print(f"Computer chose {reverseDict[computer]}\nYou chose {yourstring}")


if(computer==your):
    print("It's a tie")

else:
    if(computer==-1 and your==1):
        print("You win")
    elif(computer==-1 and your==0):
        print("You Lose")    
    elif(computer==1 and your==-1):
        print("You Lose")
    elif(computer==1 and your==0):
        print("You win")
    elif(computer==0 and your==-1):
        print("You win")
    elif(computer==0 and your==1):  
        print("You Lose")        
    else:
        print("Something went wrong!") 
       