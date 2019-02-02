from abc import ABCMeta, abstractproperty

class AbstractClass:
  __metaclass__ = ABCMeta
  
  def __init__(self):
    pass
  
  @abstractproperty
  def a(self):
    pass

class Second:
  def obshestvo(self):
    print ("Obshestvo v nachale XXI veka")
  
  def detskiiSad(self):
    print ("Vam v detskii sad")

  def shkola(self):
    print("Vam v shkolu")

  def proff(self):
    print("Vam v proffes. uchebnoe zavedenie")

  def rabota(self):
    print ("Vam na rabotu")

  def vybor(self):
    print("Vam predostavlyaetsya vybor")

  def oshibka(self):
    for i in range(5):
      print("Oshibka! Eto programma dlya lyudei")

class Final(AbstractClass, Second):
  a = 0

def main():
  test = Final()
  test.obshestvo()

  test.a = int(raw_input("Vvedite vash vozrast: "))

  if 0 <= test.a < 7:
    test.detskiiSad()
  elif 7 <= test.a < 18:
    test.shkola()
  elif 18 <= test.a < 25:
    test.proff()
  elif 25 <= test.a < 60:
    test.rabota()
  elif 60 <= test.a <= 120:
    test.vybor()
  else:
    test.oshibka()

if __name__ == "__main__":
  main()

