import sys
from aoc1.main import aoc1
from aoc2.main import aoc2
from aoc3.main import aoc3
from aoc4.main import aoc4
from aoc5.main import aoc5


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