nums = '1234567890'
sum = 0
num = 0
with open ('/workspaces/Advent-Of-Code-2023/day1/input.txt', 'r') as f:
    l = f.readlines()

for i in l:
    start = None
    end = None 
    for j in i:
        if j in nums and start == None:
            start = j
        elif j in nums and start != None:
            end = j
    if end == None:
        end = start
    num = int(start+end)
    sum += num
print(sum)
