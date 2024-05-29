def PerformBubbleSort(num):
    n = len(num)
    fixthisindex = n - 1
    while fixthisindex > 0:
      for index in range(fixthisindex):
        if num[index] > num[index + 1]:
            temp = num[index]
            num[index] = num[index + 1]
            num[index + 1] = temp
    print(num)
    fixthisindex -= 1
num=[10,8,2,14,12,7]
print("Before sorting:",num)
PerformBubbleSort(num)
print("After sorting:",num)
    
