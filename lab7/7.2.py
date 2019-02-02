import json
from pprint import pprint

with open('first.json', 'r') as data_file:
  data = json.load(data_file)
pprint(data)

sht_sum = 0
print('Kolichestvo tovarov shtukami')
for i in range(13):
  print(data['items'][i]['name']),
  print(":"),
  print(data['items'][i]['kol'])
  sht_sum = sht_sum + data['items'][i]['kol']

print("summa(shtukami): "),
print(sht_sum)

par_sum = 0
print('Kolichestvo tovarov parami')
for i in range(13):
  print(data['items'][i]['name']),
  print(":"),
  print(data['items'][i]['par'])
  par_sum = par_sum + data['items'][i]['par']

print("summa(parami): "),
print(par_sum)

new_data = {}
new_data['result'] = []
new_data['result'].append({
  'shtukami': sht_sum,
  'parami': par_sum
})
with open('second.json', 'w') as outfile:
  json.dump(new_data, outfile)

with open('second.json', 'r') as data_file:
  read_data = json.load(data_file)
pprint(read_data)
