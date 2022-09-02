
#First Task

from timeit import default_timer as timer
start = timer()
N = 10
sum = 0
for i in range(1,N+1):
    sum+=i
print(sum)
end = timer()
print(f"Execution time: {end-start}" )



#Second Task

# finding islands using recursion
def traversing(matrix, x, y, n, m):
    # if not 1 or out of range - lets skip it
    if (x < 0 or y < 0 or x >= n or y >= m or matrix[x][y] == 0):
        return
    # if catch 1, looks for neighborhood using recursion and change 1 to 0
    else:
        matrix[x][y] = 0
        traversing(matrix, x + 1, y, n, m)
        traversing(matrix, x - 1, y, n, m)
        traversing(matrix, x, y + 1, n, m)
        traversing(matrix, x, y - 1, n, m)
        return True

# count island using function traversing()
# loop through each value using a for loop
def count_islands(matrix, n, m):
    result = 0
    for i in range(n):
        for j in range(m):
            if traversing(matrix, i, j, n, m):
                result += 1
    return result


map =   [[0, 0, 0, 1],
        [0, 0, 1, 0],
        [0, 1, 0, 0]]

N = len(map)
M = len(map[0])

print(count_islands(matrix=map, n=N, m=M))
















