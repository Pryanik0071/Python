from python.bin_operations import bin


def test_to_bin():
    assert bin.to_bin(155, 2) == '10011011'
    assert bin.to_bin(2, 4) == '0010'


def test_int2hex():
    assert bin.int2hex(35) == '#23'
    assert bin.int2hex(10) == '#0a'
