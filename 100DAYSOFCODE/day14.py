from getpass import getpass as input
if __name__ == '__main__':
    print("\033[032m", "EPIC BATTLE", "\033[0m")
    print("\033[032m", "R is for rock, P is for paper, S is for scissors, ", "\033[0m")
    print("\033[032m", "Select a move (R, P, S)", "\033[0m")
    player1 = input("Player one enter (R, P ,S): ")
    player2 = input("Player two enter (R, P ,S): ")
    if player1 == "R" and player2 == "S":
        print("player one wins")
    elif player1 == "P" and player2 == "R":
        print("Player one wins")
    elif player1 == "S" and player2 == "P":
        print("player one wins")
    elif player2 == "R" and player1 == "S":
        print("Player two wins")
    elif player2 == "P" and player1 == "R":
        print("Player two wins")
    elif player2 == "S" and player1 == "P":
        print("Player two wins")
    elif player2 == player1:
        print("Draw")
    else:
        print("Try again")


