def main():
    input = open("input.txt", mode="r")
    count = 0; answer_set = set(); group_answers = []
    for line in input:
        line = line.strip()
        if not line:
            count += len(answer_set)
            answer_set.clear()
            common_elements = set.intersection(*group_answers)
            count += len(common_elements)
            group_answers.clear()
        else:
            group_answers.append(set(line))
    input.close()
    print("Solution:", count)

if __name__ == "__main__":
    main()