def acceptSeq(order="random"):
  seq = list(map(int,input("Enter a "+order+" sequence of numbers : ").split(" ")))
  val = int(input("Enter the value to be serached : "))
  return seq ,val


def acceptSeq(order="random"):
  seq = list(map(int,input("Enter a "+order+" sequence of numbers : ").split(" ")))
  val = int(input("Enter the value to be serached : "))
  return seq ,val
def linearSearch(seql,val):
  for index in range(0,len(seq)):
    print('Current Index : ',index,\
'Value at this index : ',seq[index])
if seq[index] == val:
      print('Number found at index : ',index)
      return
  print('Number not found')
seq, val = acceptSeq()
linearSearch(seq,val)

def binarySearch(seq,val):
  start,end = 0,len(seq)-1
  while start <= end:
    mid = int((start+end)/2)
    print('Current Index : ',mid,\
          'Value at this index : ',seq[mid])
    if seq[mid] == val:
      print('Number found at index : ',mid)
      return
    elif val > seq[mid]:
      start = mid+1
    elif val < seq[mid]:
      end = mid-1
  print('Number not found ')
seq, val = acceptSeq(order="sorted")
binarySearch(seq,val)

def exponentialSearch(seq,val):
  index = 1
  if seq[0] == val:
    print('Number found at index : 0')
    return
  while index < len(seq) and seq[index] < val:
    print('Current Index : ',index)
    index = index * 2
    print(index)
  binarySearch(seq,val)
def breadthFirstSearch():
  pass
def depthFirstSearch():
  pass
seq, val = acceptSeq(order="sorted")
exponentialSearch(seq,val)
