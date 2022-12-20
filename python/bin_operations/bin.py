# Число из 10ой в 2ую с count незначащих нулей
def to_bin(number, count):
    """Return bin number with count left filled '0' digits"""
    return format(number, 'b').zfill(count)


# Число из 2 в 16
def rgb2hex(r=None, g=None, b=None):
    return f'#{r:02x}{g:02x}{b:02x}'
