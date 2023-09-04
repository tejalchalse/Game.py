import random
lst=['S','W','G']
no_of_guess=1
com_ch=0 
human_ch=0
while(no_of_guess<=10):
    com_ran=random.choice(lst)
    print("Computer generated random",com_ran)
    user_in=input("Enter \n S for Snake\n W for Water\n G for Gun:")
    if user_in==com_ran:
        print("Match Draw both will get the points")
        com_ch+=1 
        human_ch+=1 
        print(f"computer chances is increase{com_ch}and human chances is increase{human_ch}")
    elif user_in =='S'and com_ran=='W':
        print("User win the 1 point")
        human_ch+=1
        print(f"human chances to win the is increase{human_ch}")
    elif com_ran =='S'and user_in=='W':
        print("computer win the 1 point")
        com_ch+=1 
        print(f"computer chances to win the is increase{com_ch} ")
    elif user_in=='W'and com_ran=='G':
        print("user win the 1 point")
        human_ch+=1
        print(f"human chances to win the is increase{human_ch}")
    elif com_ran=='W'and user_in=='G':
        print("computer win the 1 point")
        com_ch+=1 
        print(f"computer chances to win the is increase{com_ch} ")
    elif user_in=='G'and com_ran=='S':
        print("User win the 1 point")
        human_ch+=1
        print(f"human chancesto win the is increase{human_ch}")
    elif com_ran=='G'and user_in=='S':
        print("computer win the 1 point")
        com_ch+=1 
        print(f"computer chances to win the is increase{com_ch} ")
    else:
        print("You have input wrong")
    no_of_guess+=1
    print(no_of_guess," no_of_guess are done to finish the game play again ")
    
if(no_of_guess>10):
    print("Game Over")
    
if com_ch>human_ch:
    print("Computer win the game")
elif com_ch==human_ch:
    print("Match tie")
else:
    print("Human win the game")
