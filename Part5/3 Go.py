# Write your solution here
def who_won(game_board: list):
    p1_local = 0
    p2_local = 0
    for row in game_board:
        for item in row:
            if item == 1:
                p1_local += 1
            elif item == 2:
                p2_local += 1
    
    if p1_local > p2_local:
        return 1
    elif p2_local > p1_local:
        return 2
    else:
        return 0
