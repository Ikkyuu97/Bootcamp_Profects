## Pao Ying Chub (Rock Paper Scissers)
import random
choice = [0,1,2]
user_win = 0
bot_win = 0
tie = 0
count = 0
while count >=0:
    user_action = int(input("User choose 0,1,2 (rock[0], paper[1], scissors[2]): "))
    if user_action not in choice:
        print("Please enter 0,1,2 again!")
    else:
        bot_action = random.choice(choice)
        print(f"Bot choose 0,1,2 (rock[0], paper[1], scissors[2]): {bot_action}")
        if user_action == bot_action:
            print("Tie")
            tie+=1
        elif (user_action==0 and bot_action==2) or (user_action==1 and bot_action==0) \
             or (user_action==2 and bot_action==1):
            print("User win!")
            user_win+=1
        else:
            print("Bot win!")
            bot_win+=1
        end_game = input("Do you want to play again? (y/n): ").lower()
        count+=1
        if end_game=='n':break
print(f"Number of Rounds Played: {count}")
print(f"User wins: {user_win}")
print(f"Bot wins: {bot_win}")
print(f"Tie: {tie}")
if user_win+tie > bot_win+tie:result='User win!'
elif bot_win+tie > user_win+tie:result='Bot win!'
else:result='Tie'
print(f"Summarise the result of Rock Paper Scissors: {result}")
