welcome_message="""____________Welcome to our sanck water gun game hope fully you enjoy this game____________"""
print(f"{welcome_message}\n")
while(True):
    import random
    game_paticipiant=["snack","water","gun"]
    random=random.choice(game_paticipiant)
    print(random)
    print(f"The main chercter of the game is {game_paticipiant}")
    choice=input("enter one items from the above list: ")
    if(random==choice):
        print("you are tie")
    elif(choice=="snack"):
        if(random=="water"):
            print("you are win")
        else:
            print("you are fail")
    elif(choice=="water"):
        if(random=="snack"):
            print("you are fail")
        else:
            print("you are win")
    elif(choice=="gun"):
        if(random=="snack"):
            print("you are win")
        else:
            print("you are fail")