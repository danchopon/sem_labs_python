class First:
  def first(self):
    s=raw_input('input string ')
    n=int(raw_input('input numbs replays of string '))
    for element in range(n):
      print(element + 1),
      print(':'),
      print(s)

  def second(self, number):
    m=int(raw_input('input degree of number '))
    print(number**m)

  def third(self, number):
    for num in range(10):
      print(num+1),
      print(':'),
      print(number+num)
      num=num+1

  def fourth(self):
    print('INPUT ERROR!')

def main():
  test = First()
  number = int(input('input NUMBER from 1 to 9: '))
  if 1 <= number <= 3:
    test.first()
  elif 4 <= number <= 6:
    test.second(number)
  elif 7 <= number <= 9:
    test.third(number)
  else:
    test.fourth()

if __name__ == "__main__":
  main()
