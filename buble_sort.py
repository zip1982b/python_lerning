



def buble_sort(arg_list):
    number_of_swaps = 0
    print('src = {}'.format(arg_list))
    length = len(arg_list)
    for i in range(length, 0, -1):
        print('in 1 cicle')
        count = 0
        for ind in range(i-1):
            print('in 2 cicle')
            if arg_list[ind] > arg_list[ind+1]:
                number_of_swaps += 1
                count += 1
                arg_list.insert(ind+2, arg_list[ind])
                arg_list.remove(arg_list[ind])
                print(arg_list)
        if number_of_swaps == 0 or count == 0: break
    return number_of_swaps







