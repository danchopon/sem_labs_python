def spl(str):
  lst = str.split()
  for i in lst:
    print(i),
    print ('-'),
    print(len(i))

def voz(num ,arr):
  for j in range(int(num)):
    if j == 0:
      print arr[j],' ^ ',1,' = ',
      print(arr[j] ** 1)
    else:
      print arr[j],' ^ ',arr[j-1],' = ',
      print(arr[j] ** arr[j-1])
