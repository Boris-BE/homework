my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
s = len(my_list)
a = 0
while 0 < s:
    x = my_list[a]
    if 0 == x:
        a = (a + 1)
        s = (s - 1)
        continue
    elif x < 0:
        break
    print(x)
    a = (a + 1)
    s = (s - 1)


