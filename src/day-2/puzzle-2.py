file = open('src/day-2/data.txt')
data = file.readlines()
file.close()

total = 0

for line in data:
    colour_dict = {"red": 0, "green": 0, 'blue': 0}

    # Split by left and right of the ': '
    _, game_details = line.split(': ')

    # Split each turn by '; '
    turn_ls = game_details.split('; ')
    for turn in turn_ls:
        # Split by cube colour
        cubes = turn.strip().split(', ')
        # Loop through each cube pulled out
        for colour_turn in cubes:
            num, colour = colour_turn.split(' ')
            num = int(num)
            # If a new high has been reached, replace the previous high
            if num > colour_dict[colour]:
                colour_dict[colour] = num

    # Add the power to the total
    total += (colour_dict['red'] * colour_dict['blue'] * colour_dict['green'])

print(total)