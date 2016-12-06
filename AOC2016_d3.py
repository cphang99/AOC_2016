import sys

def evalT(arr): 
    if ( (arr[0] + arr[1] > arr[2]) and
        (arr[1] + arr[2] > arr[0]) and 
        (arr[0] + arr[2] > arr[1]) ):
            return 1
    else:
        print(arr)
        return 0

possibles = 0
with open('d3input.txt', 'r') as f:
    arr = []
    for line in f:
        for n in line.split():
            arr.append(int(n))
            if len(arr) == 9:
                arr1 = [arr[0], arr[3], arr[6]]
                arr2 = [arr[1], arr[4], arr[7]]
                arr3 = [arr[2], arr[5], arr[8]]
                possibles += evalT(arr1) + evalT(arr2) + evalT(arr3)
                arr = []

    print(possibles)


