input = open("input.txt", mode="r")
number_list = [int(line.strip()) for line in input]
solution = 0
for n1 in number_list:
    for n2 in number_list:
        for n3 in number_list:
            if (n1 + n2 + n3) == 2020:
                solution = n1 * n2 * n3
                break
print("Solution:", solution)
input.close()