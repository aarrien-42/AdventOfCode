input = open("input.txt", mode="r")
bags = {line.split(" contain ")[0].strip():[bag.strip().split(" ", 1) for bag in line.split(" contain ")[1].split(", ")] for line in [line.replace(".\n", '').replace("bags", '').replace("bag", '') for line in input]}
input.close()

def main():
    count = 0
    for key in bags.keys():
        count += has_shiny_gold(key)
    print("Solution:", count)

def has_shiny_gold(bag_name, it_has = False):
    if bag_name == "other":
        return it_has
    for bag in bags[bag_name]:
        if bag[1] == "shiny gold":
            it_has = True
        it_has = has_shiny_gold(bag[1], it_has)
    return it_has

if __name__ == "__main__":
    main()