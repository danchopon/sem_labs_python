print(max((str.rstrip(',.:;!?') for str in raw_input().split(';')), key=len))

