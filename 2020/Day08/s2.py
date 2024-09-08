import copy

input = open("input.txt", mode="r")
prg = [line.split() for line in [line.strip() for line in input]]
input.close()

def main():
    pc = 0; acc = 0
    for index in range(len(prg)):
        inst = prg[index][0]
        if inst == "nop" or inst == "jmp":
            new_program = copy.deepcopy(prg)
            if inst == "nop":
                new_program[index][0] = "jmp"
            if inst == "jmp":
                new_program[index][0] = "nop"
            program_ends(new_program, pc, acc)

def program_ends(program, pc = 0, acc = 0):
    while pc < len(program) and program[pc][1] != "executed":
        mem = program[pc][1]
        program[pc][1] = "executed"
        match program[pc][0]:
            case "nop":
                pc += 1
            case "acc":
                acc += int(mem)
                pc += 1
            case "jmp":
                pc += int(mem)
    if pc >= len(program):
        print("Solution:", acc)

if __name__ == "__main__":
    main()