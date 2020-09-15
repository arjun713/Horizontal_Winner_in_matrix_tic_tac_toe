# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.



game = [[1, 1, 1],
        [2, 2, 0],
        [1, 2, 0]]

def win(current_game):
    for row in game:
        print(row)
        # how might we check all items in this row? We could do something like:
        column_1 = row[0]
        column_2 = row[1]
        column_3 = row[2]
        if column_1 == column_2 == column_3:
            print("WINNER!")
win(game)