signals = ['acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab']
outputs = ['cdfeb fcadb cdfeb cdbaf']

def day8(lines):
    for line in lines:
        [signal, output] = line.split(' | ')
        signals.append(signal)
        outputs.append(output)


    zero = 0
    one = 0
    two = 0
    three = 0
    four = 0
    five = 0
    six = 0
    seven = 0
    eight = 0
    nine = 0

    for output in outputs:
        for reading in output.split(' '):
            if len(reading) == 2:
                one += 1
            if len(reading) == 4:
                four += 1
            if len(reading) == 3:
                seven += 1
            if len(reading) == 7:
                eight += 1

    print('one', one)
    print('four', four)
    print('seven', seven)
    print('eight', eight)
    print('sum', one+four+seven+eight)


    sum = 0

    for i in range(len(signals)):
        print('iteration', i)
        s = signals[i].split(' ')

        map = [None] * 7

        # 0 012456
        # 1 25
        # 2 02346
        # 3 12356
        # 4 1235
        # 5 01356
        # 6 013456
        # 7 025
        # 8 0123456
        # 9 012356

        #   0
        # 1   2
        #   3
        # 4   5
        #   6

        print(map)
        for reading in s:
            if len(reading) == 2:
                one = reading
            if len(reading) == 4:
                four = reading
            if len(reading) == 3:
                seven = reading
            if len(reading) == 7:
                eight = reading

        for c in seven:
            if not c in one:
                map[0] = c

        six_dig = []
        for _s in s:
            if len(_s) == 6:
                six_dig.append(_s)
        print(six_dig)
        for t in six_dig:
            for s in seven:
                if not s in t:
                    six = t
                    break
        for t in six_dig:

            if t != six:
                count = 0
                for s in four:
                    if s in t:
                        count += 1
                if count == 4:
                    nine = t
                else:
                    zero = t

        for c in six:
            if c not in nine:
                map[4] = c
        for c in nine:
            if c not in six:
                map[2] = c
        for c in four:
            if c not in zero:
                map[3] = c
        for s in seven:
            if s != map[0] and s != map[2]:
                map[5] = s
        for s in nine:
            if s != map[0] and s != map[2] and s != map[3] and s != map[5]:
                map[1] = s
        for s in zero:
            if s != map[0] and s != map[1] and s != map[2] and s != map[4] and s != map[5]:
                map[6] = s


        print('0 zero', zero)
        print('1 one', one)
        print('2 two', two)
        print('3 three', three)
        print('4 four', four)
        print('5 five', five)
        print('6 six', six)
        print('7 seven', seven)
        print('8 eight', eight)
        print('9 nine', nine)

        print(map)
        print('\t', map[0])
        print(map[1], '\t\t', map[2])
        print('\t', map[3])
        print(map[4], '\t\t', map[5])
        print('\t', map[6])


        output = outputs[i]
        print(output)

        numbers = []
        for o in output.split(' '):
            numbers.append(hash_to_number(o, map))
        print(numbers)
        numbers = ''.join(numbers)
        print(numbers)
        sum += int(numbers)

    print('sum', sum)


def hash_to_number(h, map):
    dig = hash_to_dig(h, map)
    print(dig)

    if len(dig) == 7 and '0' in dig and '1' in dig and '2' in dig and '3' in dig and '4' in dig and '5' in dig and '6' in dig:
        return '8'
    elif len(dig) == 7 and '0' in dig and '1' in dig and '2' in dig and '4' in dig and '5' in dig and '6' in dig:
        return '0'
    elif len(dig) == 6 and '0' in dig and '1' in dig and '3' in dig and '4' in dig and '5' in dig and '6' in dig:
        return '6'
    elif len(dig) == 6 and '0' in dig and '1' in dig and '2' in dig and '3' in dig and '5' in dig and '6' in dig:
        return '9'
    elif len(dig) == 5 and '0' in dig and '2' in dig and '3' in dig and '4' in dig and '6' in dig:
        return '2'
    elif len(dig) == 5 and '0' in dig and '2' in dig and '3' in dig and '5' in dig and '6' in dig:
        return '3'
    elif len(dig) == 5 and '0' in dig and '1' in dig and '3' in dig and '5' in dig and '6' in dig:
        return '5'
    elif len(dig) == 4 and '1' in dig and '2' in dig and '3' in dig and '5' in dig:
        return '4'
    elif len(dig) == 3 and '0' in dig and '2' in dig and '5' in dig:
        return '7'
    elif len(dig) == 2 and '2' in dig and '5' in dig:
        return '1'
    else:
        breakpoint

def hash_to_dig(h, map):
    for i in range(len(map)):
        h = h.replace(map[i], str(i))
    return h
