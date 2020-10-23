def rps():
    print("Enter \nR-rock\nS-scissor\nP-paper")
    p1 = input("player 1 enter ")
    p2 = input("player 2 enter ")


    if p1 == "R" and p2 == "S" or p1 == "S" and p2 == "P" or p1 == "P" and p2 == "R":
        print("player 1 wins")

    elif p1 == "P" and p2 == "S" or p1 == "S" and p2 == "R" or p1 == "R" and p2 == "P":
        print("player 2 wins")

    else:
        print("Game tie")

rps()
ch = input("press Y to play again and N to exit: ")
if ch == 'Y':
    rps()
else:
    print("Exit......")

