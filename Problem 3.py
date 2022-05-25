
power_2 = [pow(2,x) for x in range(22)]

def get_num(lst):

    counter = 0

    for i in range(len(lst)-1):
        for k in range(i+1,len(lst)):
            sum = lst[i] + lst[k]
            if sum in power_2:
                print(lst[i], lst[k])
                counter += 1

    return counter

print(get_num([1, 1, 1, 3, 3, 3, 7]))