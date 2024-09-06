import math

plane_long = 128
plane_wide = 8

def main():
    input = open("input.txt", mode="r")
    highest_seat_id = 0
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
            row = upper_half_long
            col = upper_half_wide
            seat_id = row * 8 + col
            if seat_id > highest_seat_id:
                highest_seat_id = seat_id
    input.close()
    print("Solution:", highest_seat_id)

if __name__ == "__main__":
    main()