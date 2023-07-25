# FROM HERE THE TOSS IS BEEN EXECUTED.
def cointoss():
    import random
    user_win=False
    choices=["h","t"]
    player_choice="0"
    toss=random.choice(choices)
# FROM HERE THE DECISION IS APPLIED WETHER THE COMPUTER WON OR USER WON.
    while player_choice not in choices:
        player_choice=input("Enter 'H' for head and 'T' for tail:\n").lower()
        if player_choice>"a" and player_choice<"z":
            player_choice=player_choice

        if player_choice==toss:
            user_win=True
        else:
            user_win=False
    
        if player_choice not in choices:
            print("Invalid input. Enter again.")
    
    return user_win 