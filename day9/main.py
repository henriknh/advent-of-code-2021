def day9(lines):
    craters = []
    basins = []

    for y in range(len(lines)):
        for x in range(len(lines[0])):

            origin = lines[y][x]
            around = []
            larger = 0
            count = 0
            crater_coords = []

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


            if len(crater_coords) > 0 and False:
                print('create coords', crater_coords)

                for crater in crater_coords:
                    potential_basin = [crater]
                    basin_sum = 0
                    visited = []

                    while len(potential_basin) > 0:
                        [y, x] = potential_basin[0]
                        visited.append(potential_basin[0])
                        potential_basin.pop(0)
                        print(y,x)
                        basin_sum += 1#int(lines[y][x])

                        for _y in [-1, 1]:
                            if _y < 0 or y+_y >= len(lines):
                                continue
                            for _x in [-1, 1]:
                                if _x < 0 or x+_x >= len(lines[0]):
                                    continue

                                if not [y+_y,x+_x] in visited and not [y+_y,x+_x] in potential_basin:
                                    potential_basin.append([y+_y, x+_x])





                    basins.append(basin_sum)



    print(craters)
    craters = [int(c) + 1 for c in craters]
    print('sum', sum(craters))

    print(basins)
