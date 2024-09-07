def main():
    input = open("input.txt", mode="r")
    count = 0; answer_set = set()
    for line in input:
        line = line.strip()
        if not line:
            count += len(answer_set)
            answer_set.clear()
        for answer in line:
            answer_set.add(answer)
    input.close()
    count += len(answer_set)
    print("Solution:", count)

if __name__ == "__main__":
    main()