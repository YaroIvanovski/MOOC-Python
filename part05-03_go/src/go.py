# Write your solution here
def who_won(game_board: list):
    player1 = 0
    player2 = 0

    for i in game_board:
        for j in i:
            if j == 1:
                player1 += 1
            elif j == 2:
                player2 += 1

    if player1 > player2:
        return 1
    if player2 > player1:
        return 2
    else:
        return 0


if __name__ == "__main__":
    x = [[1, 2, 1], [0, 1, 0], [2, 0, 0]]
    print(who_won(x))