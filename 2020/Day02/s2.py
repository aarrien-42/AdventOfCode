input = open("input.txt", mode="r")
valid_passwords = 0
for line in input:
    range, letter, password = line.split()
    letter = letter[0]
    p1, p2 = map(int, range.split('-'))
    if password[p1-1] != password[p2-1] and (password[p1-1] == letter or password[p2-1] == letter):
        valid_passwords += 1
print("Solution:", valid_passwords)
input.close()