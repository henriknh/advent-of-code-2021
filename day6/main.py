import utils

def day6(lines):
    fishes = {}
    for i in range(9):
        fishes[i] = 0

    for fish in utils.str_to_int_arr(lines[0], ','):
        fishes[fish] += 1

    for day in range(256):
        count_new = 0
        for idx in range(len(fishes)):
            if idx == 0:
                count_new = fishes[idx]
            else:
                fishes[idx - 1] = fishes[idx]
            if idx == 8:
                fishes[idx] = 0

        fishes[6] += count_new
        fishes[8] += count_new

        fish_count(day+1, fishes)

def fish_count(day, fishes):
    sum = 0
    for i in range(len(fishes)):
        sum += fishes[i]
    print("Day", day, "fishes", sum)
