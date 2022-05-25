import math

def main(flowerbed, n): 
    flowerbed = "10001"
    
    zeroes = flowerbed.split("1")

    sum = 0
    for z in zeroes:
        if z != "":
            sum += calculateSpots(len(z))
            print(z + "\n")

    return n <= sum


def calculateSpots(n):
    return math.ceil(n/2) - 1

if __name__ == "__main__":
    main()