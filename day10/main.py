import math

def day10(lines):


    error_score = 0
    incomplete_scores = []

    for line in lines:
        incomplete_score = 0
        print(line)

        for i in range(1000):
            line = line.replace('()', '')
            line = line.replace('[]', '')
            line = line.replace('{}', '')
            line = line.replace('<>', '')

        incomplete = line

        for i in range(1000):
            line = line.replace('(', '')
            line = line.replace('[', '')
            line = line.replace('{', '')
            line = line.replace('<', '')


        if len(line) > 0:
            if ')' == line[0]:
                error_score += 3
            if ']' == line[0]:
                error_score += 57
            if '}' == line[0]:
                error_score += 1197
            if '>' == line[0]:
                error_score += 25137
            print('error_score', error_score)

        else:
            print('incomplete', incomplete)
            print('incomplete', incomplete[::-1])

            for c in incomplete[::-1]:
                incomplete_score *= 5

                if c == '(':
                    incomplete_score += 1
                if c == '[':
                    incomplete_score += 2
                if c == '{':
                    incomplete_score += 3
                if c == '<':
                    incomplete_score += 4
            incomplete_scores.append(incomplete_score)

    incomplete_scores.sort()

    print(error_score)
    print(incomplete_scores)
    print(incomplete_scores[math.floor(len(incomplete_scores) / 2)])
