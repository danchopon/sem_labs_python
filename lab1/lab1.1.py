number=int(input('input NUMBER from 1 to 9: '))
if 1 <= number <= 3:
    s=raw_input('input string ')
    n=int(raw_input('input numbs replays of string '))
    for element in range(n):
        print(element + 1),
        print(':'),
        print(s)
elif 4 <= number <= 6:
    m=int(raw_input('input degree of number '))
    print(number**m)
elif 7 <= number <= 9:
    for num in range(10):
        print(num+1),
        print(':'),
        print(number+num)
        num=num+1
else:
    print('INPUT ERROR!')
