def any_alnum(string):
    a = 0 #alphabetic
    n = 0 #numeric
    for i in string:
        if i.isalpha():
            a += 1
        elif i.isdigit():
            n += 1
    if a > 0 or n > 0: return True
    else: return False

def any_alpha(string):
    a = 0
    for i in string:
        if i.isalpha():
            a += 1
    if a > 0: return True
    else: return False

def any_digits(string):
    n = 0
    for i in string:
        if i.isdigit():
            n += 1
    if n > 0: return True
    else: return False

def any_lowercase(string):
    l = 0
    for i in string:
        if i.islower():
            l += 1
    if l > 0: return True
    else: return False


def any_uppercase(string):
    u = 0
    for i in string:
        if i.isupper():
            u += 1
    if u > 0: return True
    else: return False   
      




if __name__ == '__main__':
    s = input()
    print(any_alnum(s))
    print(any_alpha(s))
    print(any_digits(s))
    print(any_lowercase(s))
    print(any_uppercase(s))

