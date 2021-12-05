def aoc3(lines):
    bits_count = len(lines[0])

    line_count = 0
    common_bits = [0 for i in range(bits_count)]

    for line in lines:
        line_count += 1
        [bits] = line.split()

        for i in range(len(bits)):
            common_bits[i] += int(str(bits)[i])

    for i in range(len(common_bits)):
        common_bits[i] = 1 if common_bits[i] > (line_count / 2) else 0

    gamma_bits = ''.join([str(i) for i in common_bits])
    gamma_value = int(gamma_bits, 2)

    epsilon_bits = ''.join(['0' if b == '1' else '1' for b in gamma_bits])
    epsilon_value = int(epsilon_bits, 2)

    print('gamma, bits', gamma_bits, 'value', gamma_value)
    print('epsilon, bits', epsilon_bits, 'value', epsilon_value)
    print('power consumption', gamma_value * epsilon_value)

    oxygen = lines
    for b in range(bits_count):
        zeros = 0
        for line in oxygen:
            [bits] = line.split()

            if bits[b] == '0':
                zeros += 1

        common = '0' if zeros > (len(oxygen) - zeros) else '1'
        oxygen = list(filter(lambda o: (o[b] == common), oxygen))

        if len(oxygen) == 1:
            break

    oxygen_value = int(oxygen[0], 2)

    co2 = []
    co2 = lines
    for b in range(bits_count):
        zeros = 0
        for line in co2:
            [bits] = line.split()

            if bits[b] == '0':
                zeros += 1

        common = '0' if zeros <= (len(co2) - zeros) else '1'
        co2 = list(filter(lambda o: (o[b] == common), co2))

        if len(co2) == 1:
            break

    co2_value = int(co2[0], 2)

    print('oxygen', 'bits', oxygen[0], 'value', oxygen_value)
    print('co2', 'bits', co2[0], 'value', co2_value)
    print('life support', oxygen_value * co2_value)
