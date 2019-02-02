import csv

file = open("first.csv", "rb")
reader = csv.DictReader(file)
data = list(reader)
for row in data:
  print(row)

sht_sum = 0
print('Kolichestvo tovarov shtukami')
for row in data:
    print(row['name']),
    print(":"),
    print(int(row['kol']))
    sht_sum = sht_sum + int(row['kol'])

print("summa(shtukami): "),
print(sht_sum)

par_sum = 0
print('Kolichestvo tovarov parami')
for row in data:
  print(row['name']),
  print(":"),
  print(int(row['kol']))
  par_sum = par_sum + int(row['par'])

print("summa(parami): "),
print(par_sum)

