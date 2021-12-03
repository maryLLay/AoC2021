#AoC 2021 Day 2

#Part 1- GOT IT RIGHT ON THE FIRST TRY!!!!
forward = 0
down = 0
up = 0

data = list(open('aoc2021_d2_data.txt'))

for entry in data:
    if 'forward' in entry:
        forward += int(entry[-2])  #only works as long as single digit numbers
    elif 'up' in entry:             #using -2 so I don't have to remove \n from data
        up += int(entry[-2])
    elif 'down' in entry:
        down += int(entry[-2])

depth = down - up


print('Your position is ', depth*forward)

#Part 2- ALSO RIGHT FIRST TRY!
aim = 0
depth = 0
hor = 0

for entry in data:
    x = int(entry[-2])
    if 'forward' in entry:
        hor += x
        depth += aim * x
    elif 'up' in entry:
        aim = aim - x
    elif 'down' in entry:
        aim += x

print(hor*depth)
