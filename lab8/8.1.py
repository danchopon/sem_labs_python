import datetime
print('1.')
string_date1 = "19901204"
print(string_date1)
date1 = datetime.datetime.strptime(string_date1, "%Y%m%d")
print(date1)

print('\n\n2.')
day1 = 17
month1 = 6
year1 = 1996
my_date = datetime.datetime(year1, month1, day1).strftime('%d.%m.%Y')
date2 = datetime.datetime.strptime(my_date,"%d.%m.%Y").strftime('%B %d, %Y')
print(date2)

print('\n\n3.')
string_date2 = "2018-05-17"
print(string_date2)
date1 = datetime.datetime.strptime(string_date2, "%Y-%m-%d")
print(date1)

print('\n\n4.')
date3 = datetime.date.today() - datetime.timedelta(1*365/12) #.isoformat()
print('Tekushaya data minus odin mesyac: '),
print(date3)

date4 = date3 + datetime.timedelta(365)
print('Novaya data plus odin god: '),
print(date4)
print('Eto'),
print(int(date4.strftime('%j'))),
print('den v godu')

print('\n\n7.')
date5 = datetime.date.today().strftime('%d.%m.%Y')
print(date5)
print(datetime.datetime.strptime(date5,"%d.%m.%Y").strftime('%B %d, %Y'))

