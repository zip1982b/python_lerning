import string


def print_rangoli(size):
    v = (size * 2) - 1
    h = ((size * 2) - 1) + (size - 1) + (size - 1)
    print(f'vertical = {v}, horizontal = {h}')
    for i in range(v//2+1):
        print((string.ascii_lowercase[(size-1)-i]).center(h, "-"))
    for l in range(v//2):
        print((string.ascii_lowercase[l+1]).center(h, "-"))





