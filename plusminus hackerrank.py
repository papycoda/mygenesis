def plusminus(arr):
    count = 0
    pos = 0
    neg = 0
    zeros = 0
    for num in arr:
        count += 1
        if num < 0:
            neg += 1
        elif num > 0:
            pos += 1
        else:
            zeros += 1
    print (pos/count,"\n ",neg/count,"\n", zeros/count)
