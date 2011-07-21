import string
bound = 20
big = 0

def adjacent(arr, x, y):
    big = 0
    temp = 0

    #right
    if y < 17:
        temp = int(arr[x][y]) * int(arr[x][y+1]) * int(arr[x][y+2]) * int(arr[x][y+3])
        if temp > big: big = temp
    #down
    if x < 17:
        temp = int(arr[x][y]) * int(arr[x+1][y]) * int(arr[x+2][y]) * int(arr[x+3][y])
        if temp > big: big = temp
    #diagonal right
    if x < 17 and y < 17:
        temp = int(arr[x][y]) * int(arr[x+1][y+1]) * int(arr[x+2][y+2]) * int(arr[x+3][y+3])
        if temp > big: big = temp
    #diagonal left
    if 3 < x and y < 17:
        temp = int(arr[x][y]) * int(arr[x-1][y+1]) * int(arr[x-2][y+2]) * int(arr[x-3][y+3])
        if temp > big: big = temp
    return big

array = []
f = open('euler11', 'r')
for line in f:
    array.append(line.split())

for x in range(bound):
    for y in range(bound):
       big = max(adjacent(array, x, y), big)

print big

f.close()
