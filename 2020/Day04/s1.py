def main():
    input = open("input.txt", mode="r")
    valid_passports = 0; passport = {}; passport_list = []
    for line in input:
        line = line.strip()
        if line:
            passport.update({key:value for key, value in [pair.split(':') for pair in line.split()]})
        else:
            passport_list.append(passport)
            passport = {}
    passport_list.append(passport)
    passport = {}

    for passport in passport_list:
        if is_passport_valid(passport):
            valid_passports += 1

    print("Solution:", valid_passports)
    input.close()

def is_passport_valid(passport):
    required_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    field_num = 0
    for key in passport.keys():
        if key in required_fields:
            field_num += 1
    if field_num == 7:
        return True
    return False


if __name__ == "__main__":
    main()