def str_to_arr(str, sep=' '):
    return list(filter(lambda s: s != '', str.split(sep)))


def str_to_int_arr(str: str, sep=' '):
    return [int(i.strip()) for i in str_to_arr(str, sep)]
