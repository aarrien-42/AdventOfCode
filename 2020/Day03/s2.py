input = open("input.txt", mode="r")
forest = [line.strip() for line in input]
height = len(forest)
width = len(forest[0])
input.close()

def count_trees(step_right, step_down):
    trees = 0; x = 0
    for y in range(step_down, height, step_down):
        x += step_right
        if x >= width:
            x -= width
        if forest[y][x] == '#':
            trees += 1
    return trees

def main():
    print("Solution:", count_trees(1, 1) * count_trees(3, 1) * count_trees(5, 1) * count_trees(7, 1) * count_trees(1, 2))

if __name__ == "__main__":
    main()
