def my_print(a):
  if 0 <= a < 7:
    print ("Vam v detskii sad")
  elif 7 <= a < 18:
    print("Vam v shkolu")
  elif 18 <= a < 25:
    print ("Vam v proffes. uchebnoe zavedenie")
  elif 25 <= a < 60:
    print ("Vam na rabotu")
  elif 60 <= a <= 120:
    print ("Vam predostavlyaetsya vybor")
  else:
    for i in range(5):
      print("Oshibka! Eto programma dlya lyudei")
