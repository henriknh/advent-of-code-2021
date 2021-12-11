import sys
from day1.main import day1
from day2.main import day2
from day3.main import day3
from day4.main import day4
from day5.main import day5
from day6.main import day6
from day7.main import day7
from day8.main import day8
from day9.main import day9
from day10.main import day10
from day11.main import day11

if len(sys.argv) < 2:
    print('choose aoc day')
else:
    aoc_day = sys.argv[1]
    filename = 'data'

    if len(sys.argv) == 3 and sys.argv[2] == 'debug':
        print('DEBUG MODE!')
        filename = 'data_test'
    file = open('/'.join([aoc_day, filename]), 'r')
    lines = file.readlines()
    lines = [line.strip() for line in lines]

    print('Running', aoc_day)
    globals()[aoc_day](lines)
