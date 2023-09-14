
# [
# [1,2,3], 
# [4,5,6], 
# [7,8,9]
# ]

def all_same(items = []):
    if items[0] == items[1] and items[1] == items[2] and items[0] != " " and items[0] != 0:
        return True
    else:
        return False

# rearrange the possible combination
def possibilities_align(horizondal_box=[]):

    # vertical checker
    vertical_box = []
    for i in range(3):
        vertical_box.append([x[i] for x in horizondal_box])
    
    # diagnol checker
    diagnol_box = [[horizondal_box[i][i] for i in range(3)], [horizondal_box[i][2-i] for i in range(3)]]
    
    return horizondal_box, vertical_box, diagnol_box

def win_checker(box):
    
    win = False
    possibilities = possibilities_align(box)

    # check horizondal
    for possible_box in possibilities:
        if not win:
            for possible in possible_box:
                if all_same(possible):
                    win = True
                    break
        if win:
            break

    return win
