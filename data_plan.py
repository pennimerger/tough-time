"""MTN Data Platform"""
import MTN_Data_Plan as mdp
prompt = "You dialed *131#"
prompt += "\nPress enter to choose a plan."
user = input(prompt)
if user.lower() == "":
    _user = mdp.choice()
    if _user == 1:
        lent = mdp.weekly()
        user_ = int(input("Select plan _"))
        if user_ in range(1,lent):
            mdp.bundle()
        else:
            print("Invalid response, try again.")
    elif _user == 2:
        _lent = mdp.monthly()
        user_ = int(input("\nSelect plan _"))
        if user_ in range(1,_lent):
            mdp.bundle()
        else:
            print("Invalid response, try again.")
    else:
        print("Invalid response, try again.")
else:
    print("Invalid response, try again.")