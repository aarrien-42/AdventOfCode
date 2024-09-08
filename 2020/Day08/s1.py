input = open("input.txt", mode="r")
program = [line.split() for line in [line.strip() for line in input]]
input.close()

def main():
    pc = 0; acc = 0
    while program[pc][1] != "0":
        mem = program[pc][1]
        program[pc][1] = "0"
        match program[pc][0]:
            case "nop":
                pc += 1
            case "acc":
                acc += int(mem)
                pc += 1
            case "jmp":
                pc += int(mem)
    print("Solution:", acc)

if __name__ == "__main__":
    main()