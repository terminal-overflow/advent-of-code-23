# Load the file in
file = open('src/day-1/data.txt')
data = file.readlines()
file.close()

# Establish 1-9 words as numbers
num_word_ls = ['one', 'two', 'three', 'four', 'five',
               'six', 'seven', 'eight', 'nine']

# Loop through each item
total = 0
for item in data:
    # Initialise tuple list
    # Tuple format looks like (index found in item, value)
    tuple_ls = []

    # Loop through each num_word_ls
    for num, word in enumerate(num_word_ls, 1):
        # mark each instance of the word
        indices = [i for i in range(len((item))) if item.startswith(word, i)]
        # if word in item:
        for i in range(len(indices)):
            tuple_ls.append((indices[i], str(num)))

    for c in item:
        # Check if character is digit
        if c.isdigit():
            # mark each instance of the number
            indices = [i for i in range(len((item))) if item.startswith(c, i)]
            for i in range(len(indices)):
                tuple_ls.append((indices[i], c))
    total += int(min(tuple_ls)[1] + max(tuple_ls)[1]) if len(tuple_ls) > 1 else int(tuple_ls[0][1] + tuple_ls[0][1])

print(total)