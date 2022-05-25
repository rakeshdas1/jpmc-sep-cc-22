flowerbed = [1,0,0,0,1]
n = 2

def solution(arr, n):
    if n == 0:
        return True
    elif n > 0:
        for i in range(1,len(arr) - 1):
            if arr[i] == 0 and arr[i - 1] != 1 and arr[i + 1] != 1:
                arr[i] = 1
                n -= 1
        if n == 0:
            return True
        if n > 0:
            return False
                
    return True

print(solution(flowerbed, n))