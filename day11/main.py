def day11(lines):
    flashes = 0
    for i in range(len(lines)):
        lines[i] = [int(c) for c in lines[i]]

    print_grid(lines)

    for i in range(2000):
        print('Step', i+1)
        increase_energy_level(lines)
        handle_flashes(lines)

        flashes += count_flashes(lines)

        print_grid(lines)
        print('Flashes:', flashes)

def print_grid(lines):
    print('GRID:')
    for line in lines:
        print(''.join([str(i) for i in line]))

def increase_energy_level(lines):
    for y in range(len(lines)):
        for x in range(len(lines[0])):
            lines[y][x] = lines[y][x] + 1

def handle_flashes(lines):
    to_flash = []
    for y in range(len(lines)):
        for x in range(len(lines[0])):
            if lines[y][x] == 10:
                to_flash.append([y,x])

    for [y,x] in to_flash:
        do_flash(lines, y, x)

def do_flash(lines, y, x):
    for _y in [y-1, y, y+1]:
        for _x in [x-1, x, x+1]:
            if _y == y and _x == x:
                continue
            elif _y < 0:
                continue
            elif _x < 0:
                continue
            elif _y >= len(lines):
                continue
            elif _x >= len(lines[0]):
                continue
            else:
                before = lines[_y][_x]
                lines[_y][_x] += 1

                if before == 9 and lines[_y][_x] == 10:
                    do_flash(lines, _y, _x)

def count_flashes(lines):
    count = 0
    total_possible = len(lines) * len(lines[0])
    for y in range(len(lines)):
        for x in range(len(lines[0])):
            if lines[y][x] > 9:
                count += 1
                lines[y][x] = 0
    print(count, total_possible)
    if count == total_possible:
        raise NameError('ALL FLASHES')
    return count
