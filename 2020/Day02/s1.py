input = open("input.txt", mode="r")
valid_passwords = 0
for line in input:
    range, letter, password = line.split()
    letter = letter[0]
    min, max = map(int, range.split('-'))
    if min <= password.count(letter) <= max:
        valid_passwords += 1
print("Solution:", valid_passwords)
input.close()