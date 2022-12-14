# Число из 10ой в 2ую с count незначащих нулей
def to_bin(number, count):
    """Return bin number with count left filled '0' digits"""
    return format(number, 'b').zfill(count)