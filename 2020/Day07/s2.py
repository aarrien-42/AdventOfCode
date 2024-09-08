input = open("input.txt", mode="r")
bags = {line.split(" contain ")[0].strip():[bag.strip().split(" ", 1) for bag in line.split(" contain ")[1].split(", ")] for line in [line.replace(".\n", '').replace("bags", '').replace("bag", '') for line in input]}
input.close()

def main():
    count = bag_count("shiny gold")
    print("Solution:", count)

def bag_count(bag_name, count = 0):
    for bag in bags[bag_name]:
        if (bag[0].isdigit()):
            if has_more_bags(bag[1]):
                count += int(bag[0]) + bag_count(bag[1])*int(bag[0])
            else:
                count += int(bag[0])
    return count

def has_more_bags(bag_name):
    if len(bags[bag_name]) == 1 and bags[bag_name][0][1] == "other":
        return False
    return True

if __name__ == "__main__":
    main()