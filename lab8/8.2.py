import datetime

n = int(raw_input("Enter your number in range 1 - 365: "))

a = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

if n > 365 or n < 1:
  print("Enter number only in range 1 - 365 !!!! ")
else:
  k = 1
  while a[k-1] < n:
    n = n - a[k-1]
    k += 1

date = datetime.datetime(year=1900, month=k, day=n).strftime('%d.%m.%Y')
print(date)
formatted_date = datetime.datetime.strptime(date,"%d.%m.%Y").strftime('%B %d, %Y')
print(formatted_date)
