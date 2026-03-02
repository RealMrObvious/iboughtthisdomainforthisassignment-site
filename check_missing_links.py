import re

with open('outgoinglinks.txt', 'r') as file:
    txt = file.read()

# Extract everything inside brackets
matches = re.findall(r'\[(.*?)\]', txt)

# Extract all numbers from those matches
numbers = set()
for match in matches:
    numbers.update(int(n.strip()) for n in match.split(','))

# Check which numbers from 0–499 are missing
for i in range(500):
    if i not in numbers:
        print(f'{i} missing')