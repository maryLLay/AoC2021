#AoC2021 Day 1, Problem 1

data = list(open('aoc2021_d1_data.txt'))
my_data = [int(y) for y in data]  #must convert to int; otherwise, wrong answer

#version 1
increase = 0
for x in range(0, len(my_data)):
    if my_data[x]>my_data[x-1]:
        increase+=1

print(increase)

#version 2
increase = 0
for x in range (0, len(my_data)+1):
    try:
        if my_data[x]<my_data[x+1]:
            increase+=1
    except:
        pass
print(increase)

#version 3- still doesn't work
increase= 0
prevnum = 100000000
for x in range (1, len(my_data)-1):
    if prevnum < int(my_data[x]):
        increase+=1
    prevnum = int(my_data[x])
print(increase)


#NOT 1713
#stolen version 4- Reddit
with open('aoc2021_d1_data.txt') as f:
    data = [int(x) for x in f]

print(sum(x < y for x, y in zip(data, data[1:]))) #What does zip do??
print(sum(x < y for x, y in zip(data, data[3:])))


#Part 2
increase = 0
for x in range(0, len(my_data)):
    j = sum(my_data[x:x+3])
    k = sum(my_data[x-1:x+2])
    if sum(my_data[x+1:x+4])>sum(my_data[x:x+3]):
        increase+=1
    else:
        continue
print(increase)
