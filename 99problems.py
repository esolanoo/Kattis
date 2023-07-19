x = int(input())
if x<100:
    print(99)
else:
    s = int(str(x)[-2:])
    if 99-s > 50:
        print(int(str(x)[:-2]+"00")-1)
    else:
        print(int(str(x)[:-2]+"00")+99)