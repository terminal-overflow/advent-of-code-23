file = open('src/day-2/data.txt')
data = file.readlines()
file.close()

limit_dict = {"RED": 12, "GREEN": 13, "BLUE": 14}

total = 0

for line in data:
    breached = False

    # Split by left and right of the ': '
    game, game_details = line.split(': ')
    game_id = int(game.split(' ')[1])

    # Split each turn by '; '
    turn_ls = game_details.split('; ')
    for turn in turn_ls:
        # Split by cube colour
        cubes = turn.strip().split(', ')
        # Loop through each cube pulled out and compare against the limit for that colour
        breached = True if [number for number in cubes if int(number.split(' ')[0]) > limit_dict.get(number.split(' ')[1].upper())] != [] else False
        if breached: break

    if not breached:
        total += game_id

print(total)