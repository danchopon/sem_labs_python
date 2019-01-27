#это нужно вводить в интерактивном режиме
#ищет самое короткое слово
s = 'Happy day has come to us'
l = s.split()
min(l, key=len)
