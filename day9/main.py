import math

def day9(lines):
    craters = []
    crater_coords = []
    basins = []

    for y in range(len(lines)):
        for x in range(len(lines[0])):

            origin = lines[y][x]
            around = []
            larger = 0
            count = 0

            if y-1 >= 0:
                around.append(lines[y-1][x])
                count += 1
            if y+1 < len(lines):
                around.append(lines[y+1][x])
                count += 1
            if x-1 >= 0:
                around.append(lines[y][x-1])
                count += 1
            if x+1 < len(lines[0]):
                around.append(lines[y][x+1])
                count += 1

            for a in around:
                if a > origin:
                    larger +=1

            if larger == count:
                craters.append(origin)
                crater_coords.append([y,x])


    if len(crater_coords) > 0:
        print('create coords', crater_coords)

        for crater in crater_coords:
            potential_basin = [crater]
            basin_sum = 0
            visited = []

            while len(potential_basin) > 0:
                print(potential_basin)
                [y, x] = potential_basin[0]
                visited.append(potential_basin[0])
                potential_basin.pop(0)
                print(y,x, lines[y][x])
                if int(lines[y][x]) != 9:
                    basin_sum += 1#int(lines[y][x])
                    print(basin_sum)


                    for coord in [[y-1,x], [y+1,x], [y, x-1], [y, x+1]]:
                        [_y, _x] = coord
                        if _y < 0 or _y >= len(lines):
                            continue
                        if _x < 0 or _x >= len(lines[0]):
                            continue

                        if not [_y,_x] in visited and not [_y,_x] in potential_basin:
                            potential_basin.append([_y,_x])

            basins.append(basin_sum)



    print(craters)
    craters = [int(c) + 1 for c in craters]
    print('sum', sum(craters))

    basins.sort(reverse=True)
    print(basins)

    largest = basins[:3]
    print(largest)

    print(math.prod(largest))
