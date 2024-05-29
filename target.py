num=[10,20,30,37,43]
target=30
flage=-1
n=len(num)
for index in range(n):
   if num[index] == target:
      flage=index
      break 
   if flage == -1:
      print("not found")
   else:
      print("target found at:",flage)
