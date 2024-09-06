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

def is_byr_valid(value):
    if len(value) == 4 and value.isdigit():
        num = int(value)
        if 1920 <= num <= 2002:
            return True
    return False

def is_iyr_valid(value):
    if len(value) == 4 and value.isdigit():
        num = int(value)
        if 2010 <= num <= 2020:
            return True
    return False

def is_eyr_valid(value):
    if len(value) == 4 and value.isdigit():
        num = int(value)
        if 2020 <= num <= 2030:
            return True
    return False

def is_hgt_valid(value):
    if value.endswith("cm") or value.endswith("in"):
        num = value[:len(value)-2]
        if num.isdigit():
            if value.endswith("cm") and (150 <= int(num) <= 193):
                return True
            if value.endswith("in") and (59 <= int(num) <= 76):
                return True
    return False

def is_hcl_valid(value):
    if value[0] == '#':
        for index in range(1, len(value)):
            if not value[index].isdigit() and not ('a' <= value[index] <= 'f'):
                return False
        return True
    return False

def is_ecl_valid(value):
    valid_colors = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    if value in valid_colors:
        return True
    return False

def is_pid_valid(value):
    if value.isdigit() and len(value) == 9:
        return True
    return False

def is_passport_valid(passport):
    required_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    field_num = 0
    for key, value in passport.items():
        if key in required_fields:
            match key:
                case "byr":
                    field_num += is_byr_valid(value)
                case "iyr":
                    field_num += is_iyr_valid(value)
                case "eyr":
                    field_num += is_eyr_valid(value)
                case "hgt":
                    field_num += is_hgt_valid(value)
                case "hcl":
                    field_num += is_hcl_valid(value)
                case "ecl":
                    field_num += is_ecl_valid(value)
                case "pid":
                    field_num += is_pid_valid(value)
    if field_num == 7:
        return True
    return False


if __name__ == "__main__":
    main()