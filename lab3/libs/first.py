def input(number):
  if 1 <= number <= 3:
    output1()
  elif 4 <= number <= 6:
    output2(number)
  elif 7 <= number <= 9:
    output3(number)
  else:
    print('INPUT ERROR!')

def output1():
  s=raw_input('input string ')
  n=int(raw_input('input numbs replays of string '))
  a = [s for element in range(n)]
  print a

def output2(numb):
  m=int(raw_input('input degree of number '))
  print(numb**m)

def output3(numb):
  a = [numb + num for num in range(10)]
  print a
