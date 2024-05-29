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


