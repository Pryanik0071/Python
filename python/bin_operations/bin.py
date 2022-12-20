# Число из 10ой в 2ую с count незначащих нулей
def to_bin(number, count):
    """Return bin number with count left filled '0' digits"""
    return format(number, 'b').zfill(count)


# Число из 10ой в 16ую до 2-х незначащих нулей
def int2hex(r=None):
    """Return hex number from int with 2 left filled '0' digits"""
    return f'#{r:02x}'
