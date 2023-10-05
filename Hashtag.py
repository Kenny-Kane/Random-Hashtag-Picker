import random

# Specify the path to your text file
file_path = 'your_text_file.txt'

# Open the file for reading
with open(file_path, 'r') as file:
    # Read all the lines into a list
    lines = file.readlines()

# Check if there are at least 30 lines in the file
if len(lines) < 30:
    print("The file doesn't have enough lines.")
else:
    # Use random.sample to select 30 unique random lines from the list of lines
    random_lines = random.sample(lines, 30)

    # Print the selected random lines
    for line in random_lines:
        print(line.strip())
