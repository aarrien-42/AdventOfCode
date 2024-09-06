import math

plane_long = 128
plane_wide = 8

def main():
    input = open("input.txt", mode="r")
    seat_id_list = []
    for line in input:
        line = line.strip()
        lower_half_long = 0; upper_half_long = 127; lower_half_wide = 0; upper_half_wide = 7
        row = 0; col = 0; seat_id = 0
        for long_index in range(len(line)):
            match line[long_index]:
                case 'F':
                    upper_half_long = math.floor(upper_half_long - (upper_half_long - lower_half_long) / 2)
                case 'B':
                    lower_half_long = math.ceil(lower_half_long + (upper_half_long - lower_half_long) / 2)
                case 'R':
                    lower_half_wide = math.ceil(lower_half_wide + (upper_half_wide - lower_half_wide) / 2)
                case 'L':
                    upper_half_wide = math.floor(upper_half_wide - (upper_half_wide - lower_half_wide) / 2)
        if upper_half_long == lower_half_long and upper_half_wide == lower_half_wide:
            seat_id_list.append(upper_half_long * 8 + upper_half_wide)
    input.close()

    seat_id_list.sort()
    for seat in range(seat_id_list[0], seat_id_list[len(seat_id_list) - 1]):
        if seat not in seat_id_list:
            print("Solution:", seat)

if __name__ == "__main__":
    main()