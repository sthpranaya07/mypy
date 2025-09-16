# ===== WARNING: THIS PROGRAM STILL HAS SOME MINOR ERRORS =====

from tabulate import tabulate
from random import choice
from os import system

def main():
    board = [
        [" ", " ", " "], 
        [" ", " ", " "], 
        [" ", " ", " "]
        ]
    
    choices = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    user_moves = []
    computer_moves = []
    userWin = False
    computerWin = False

    while True:
        user_choose_x_or_o = input("Choose 'o' or 'x': ").strip().upper()

        if user_choose_x_or_o == "X":
            user = "X"
            computer = "O"
            break
        elif user_choose_x_or_o == "O":
            user = "O"
            computer = "X"
            break
        else:
            print("Invalid option! Try again")

    system('cls')

    while choices:
        print(tabulate(board, tablefmt="simple_grid"))

        user_input = int(input("Choose from <1-9>: "))
        if user_input not in choices:
            print("Invalid move! Try again.")
            continue

        choices.remove(user_input)
        user_moves.append(user_input)

        row = (user_input - 1) // 3
        col = (user_input - 1) % 3
        board[row][col] = user

        if not choices:
            break

        computer_input = choice(choices)
        choices.remove(computer_input)
        computer_moves.append(computer_input)

        row = (computer_input - 1) // 3
        col = (computer_input - 1) % 3
        board[row][col] = computer

        winning_lines = [
            # rows
            [board[0][0], board[0][1], board[0][2]],
            [board[1][0], board[1][1], board[1][2]],
            [board[2][0], board[2][1], board[2][2]],
            # columns
            [board[0][0], board[1][0], board[2][0]],
            [board[0][1], board[1][1], board[2][1]],
            [board[0][2], board[1][2], board[2][2]],
            # diagonals
            [board[0][0], board[1][1], board[2][2]],
            [board[0][2], board[1][1], board[2][0]]
        ]

        system('cls')

        for line in winning_lines:
            if line == [user, user, user]:
                print(tabulate(board, tablefmt="simple_grid"))
                print("You win 🎉")
                userWin = True
                break
            elif line == [computer, computer, computer]:
                print(tabulate(board, tablefmt="simple_grid"))
                print("You lost 🏳")
                computerWin = True
                break

        if userWin or computerWin:
            break
    
    if not userWin and not computerWin:
            print(tabulate(board, tablefmt="simple_grid"))
            print("It's a draw 🤝")


if __name__ == "__main__":
    main()