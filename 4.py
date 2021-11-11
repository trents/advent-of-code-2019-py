""" Solution to Day 4 of 2019 Advent of Code - https://adventofcode.com/2019/day/4 """

with open('4.txt') as f:
    lines = f.readlines()
f.close()

lownum, highnum = lines[0].split("-")
lownum = int(lownum)
highnum = int(highnum)

password_count = 0
password_count_b = 0

for i in range(lownum, highnum+1):
    condition1 = False
    condition2 = False
    condition3 = False
    condition4 = False
    condition5 = False

    if 99999 < i < 1000000:
        condition1 = True

    if lownum <= i <= highnum:
        condition2 = True

    stri = str(i)

    if condition1:
        if stri[0] == stri[1] or stri[1] == stri[2] or stri[2] == stri[3] or stri[3] == stri[4] or stri[4] == stri[5]:
            condition3 = True

    if condition1:
        if int(stri[0]) <= int(stri[1]) and int(stri[1]) <= int(stri[2]) and int(stri[2]) <= int(stri[3]) and int(stri[3]) <= int(stri[4]) and int(stri[4]) <= int(stri[5]):
            condition4 = True

    if condition1:
        if int(stri[0]) == int(stri[1]) and int(stri[1]) != int(stri[2]):
            condition5 = True
        elif int(stri[0]) != int(stri[1]) and int(stri[1]) == int(stri[2]) and int(stri[2]) != int(stri[3]):
            condition5 = True 
        elif int(stri[1]) != int(stri[2]) and int(stri[2]) == int(stri[3]) and int(stri[3]) != int(stri[4]):
            condition5 = True
        elif int(stri[2]) != int(stri[3]) and int(stri[3]) == int(stri[4]) and int(stri[4]) != int(stri[5]):
            condition5 = True
        elif int(stri[4]) == int(stri[5]) and int(stri[3]) != int(stri[4]):
            condition5 = True

    if condition1 and condition2 and condition3 and condition4:
        password_count += 1
    if condition1 and condition2 and condition3 and condition4 and condition5:
        password_count_b += 1

print("4a ->",password_count)
print("4b ->",password_count_b)
