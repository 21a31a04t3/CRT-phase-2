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

