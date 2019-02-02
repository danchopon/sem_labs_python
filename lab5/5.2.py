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

def main():
  test = Second()
  test.obshestvo()

  a = int(raw_input("Vvedite vash vozrast: "))

  if 0 <= a < 7:
    test.detskiiSad()
  elif 7 <= a < 18:
    test.shkola()
  elif 18 <= a < 25:
    test.proff()
  elif 25 <= a < 60:
    test.rabota()
  elif 60 <= a <= 120:
    test.vybor()
  else:
    test.oshibka()

if __name__ == "__main__":
  main()

