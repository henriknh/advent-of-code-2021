def aoc2(lines):
    x = 0
    y = 0 

    for line in lines:
        [dir, value] = line.split()

        if dir == 'forward':
            x += int(value)
        elif dir == 'down':
            y += int(value)
        elif dir == 'up':
            y -= int(value)

    print("X:", x, "Y:", y, "sum:", x*y)

    x = 0
    y = 0 
    aim = 0

    for line in lines:
        [dir, value] = line.split()

        if dir == 'forward':
            x += int(value)
            y += aim * int(value)
        elif dir == 'down':
            #y += int(value)
            aim += int(value)
        elif dir == 'up':
            #y -= int(value)
            aim -= int(value)

    print("X:", x, "Y:", y, "sum:", x*y)