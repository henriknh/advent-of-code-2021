def aoc1(lines):
    count = 0
    prev = 9999999

    for line in lines:
        if prev:
            curr = int(line)
            if prev < curr:
                count += 1
        prev = curr

    print('A')
    print(count)

    count = 0

    slide = []

    for line in lines:

        prev = 999999
        curr = 999998

        if len(slide) == 3:
            prev = slide[0] + slide[1] + slide[2]
            
            slide.pop(0)
        if len(slide) < 3:
            slide.append(int(line))

        if len(slide) == 3:
            curr = slide[0] + slide[1] + slide[2]

        if prev < curr:
            count += 1
        
    print('B')
    print(count)