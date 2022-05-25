
power_2 = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288, 1048576, 2097152]

def get_num(lst):

    counter = 0

    for i in range(len(lst)-1):
        for k in range(i+1,len(lst)):
            sum = lst[i] + lst[k]
            if sum in power_2:
                counter += 1

    return counter

print(power_2)