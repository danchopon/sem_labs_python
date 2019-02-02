from abc import ABCMeta, abstractproperty

class AbstractClass:
  __metaclass__ = ABCMeta
    
  def __init__(self):
    pass

  @abstractproperty
  def number(self):
    pass

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

class Final(AbstractClass, First):
  number = 0

def main():
  test = Final()
  test.number = int(input('input NUMBER from 1 to 9: '))
  if 1 <= test.number <= 3:
    test.first()
  elif 4 <= test.number <= 6:
    test.second(test.number)
  elif 7 <= test.number <= 9:
    test.third(test.number)
  else:
    test.fourth()


if __name__ == "__main__":
  main()
