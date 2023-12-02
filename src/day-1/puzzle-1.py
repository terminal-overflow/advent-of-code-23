# Load the file in
file = open('resources/day-1/puzzle-1.txt')
data = file.readlines()
file.close()

# Loop through each item
total = 0
for item in data:
    first_num = ''
    last_num = ''
    for c in item:
        # Check if character is digit
        if c.isdigit():
            if first_num == '':
                first_num = c
            last_num = c
    total += int(first_num + last_num)

print(total)