def print_formatted(number):
    # your code goes here
    s = format(number, 'b')
    width = len(str(number))
    width_bin = len(s)
    print(width)
    space = ' '




    for i in range(1, number+1):
        print(f'{i:2d}'+width*space+f'{i:2o}'+width*space+f'{i:2X}'+ f' {i:{width_bin}b}')
        

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)


