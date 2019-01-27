number=int(input('input NUMBER from 1 to 9: '))
if 1 <= number <= 3:
  s=raw_input('input string ')
  n=int(raw_input('input numbs replays of string '))
  a = [s for element in range(n)]
  print a
elif 4 <= number <= 6:
  m=int(raw_input('input degree of number '))
  print(number**m)
elif 7 <= number <= 9:
  a = [number + num for num in range(10)]
  print a
else:
  print('INPUT ERROR!')


