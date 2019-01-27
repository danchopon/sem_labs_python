import libs

num_array = list()
num = raw_input("Enter how many elements you want:")
print 'Enter numbers in array: '
for i in range(int(num)):
  print(i+1),
  n = raw_input("num:")
  num_array.append(int(n))
print 'ARRAY: ',num_array

libs.voz(num, num_array)


