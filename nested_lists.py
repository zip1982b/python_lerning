
def buble_sort(l):
    number_of_swaps = 0
    length = len(l)
    for i in range(length, 0, -1):
        count = 0
        for ind in range(i-1):
            if l[ind][1] > l[ind+1][1]:
                number_of_swaps += 1
                count += 1
                l.insert(ind+2, l[ind])
                l.remove(l[ind])
        if number_of_swaps == 0 or count == 0: break





if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.extend([[name, score]])
    buble_sort(students)
    print(students)
    scores = [i[1] for i in students]
    print(f'scores = {scores}')
    m = min(scores)
    print(f'minimum score = {m}')
    for h in scores:
        print(f'h = {h}')
        if h == m:
            print(f'delete {h}')
            scores.remove(h)
    print(f'scores = {scores}')

    second_lowest = min(scores)
    print(f'second lowest = {second_lowest}')
    for_print = [t[0] for t in students if t[1] == second_lowest]
    print(for_print)


