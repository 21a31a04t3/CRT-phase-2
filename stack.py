def push(stack, ele):
    stack.append(ele)
    print(ele, "inserted into stack sucessfully")

def pop(stack):
    if len(stack) == 0:
      print("stack is empty")
      return
    print(stack[-1],"delete sucessfully")
    stack.pop()

stack = []
push(stack,10)
push(stack,20)
push(stack,30)

pop(stack)
pop(stack)
pop(stack)



def enquequ(Q,ele):
   Q.append(ele)
   print(ele,"inserted into stack successfully")
   
   
def dequequ(Q):
   if len(Q) ==0:
      print("Quequ is empty")
      return
   print(Q[0],"is getting deleted")
   Q.pop(0)
Queque =[]

enquequ(Queque,10)
enquequ(Queque,20)
enquequ(Queque,30)
enquequ(Queque,40)

dequequ(Queque)
dequequ(Queque)
dequequ(Queque)
dequequ(Queque)




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






nums=[6,10,12,23,47]
target=10
nums=sorted (nums)
left=0
right=len(nums)-1
flage=-1
while left <=right:
   mid=(left+right) //2
   if nums[mid] == target:
      flage=mid
      break
   elif nums[mid] > target:
    right= mid - 1
   else:
      left =mid + 1
   if flage == -1:
      print("target not found")
   else:
      print("target found at index:",flage)














   




