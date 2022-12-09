f = open('2022/day 2/values.txt','r')
file = f.read()
values = file.split('\n')
score = 0

for i in range (len(values)):
    if values[i][0] == 'A':
        player1 = 1
    elif values[i][0] == 'B':
        player1 = 2
    else:
        player1 = 3
    if values[i][2] == 'X':
        player2 = 1
    elif values[i][2] == 'Y':
        player2 = 2
    else:
        player2 = 3
    score += player2

    if player1 == 1:
        if player2 == 2:
            match = 6
        elif player2 == 3:
            match = 0
        else:
            match = 3
    elif player1 == 2:
        if player2 == 3:
            match = 6
        elif player2 == 1:
            match = 0
        else:
            match = 3
    else:
        if player2 == 1:
            match = 6
        elif player2 == 2:
            match = 0
        else:
            match = 3
    score += match

print(score)