input = open("input.txt", mode="r")
forest = [line.strip() for line in input]
height = len(forest)
width = len(forest[0])
step_right = 3; step_down = 1; trees = 0; x = 0
for y in range(step_down, height, step_down):
    x += step_right
    if x >= width:
        x -= width
    if forest[y][x] == '#':
        trees += 1
print("Solution:", trees)
input.close()