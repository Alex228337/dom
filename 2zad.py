l = []
with open('mat_dv.txt', 'r') as f:
    l = f.read().splitlines()
print(l)
for i in l:
    l = i.split()
    print(l)
    l[2] = int(l[2])
    l[3] = int(l[3])
    l[4] = int(l[4])
    if 9>l[2]>7  :
        maxv = 0
        print(l[2])
        for i in l:
            if l[3]+l[4] > maxv:
                maxv = l[3]+l[4]
    if 10>l[2]>8  :
        maxv1 = 0
        print(l[2])
        for i in l:
            if l[3]+l[4] > maxv1:
                maxv1 = l[3]+l[4]
    if 11>l[2]>9  :
        maxv2 = 0
        print(l[2])
        for i in l:
            if l[3]+l[4] > maxv2:
                maxv2 = l[3]+l[4]
    if 12>l[2]>10  :
        maxv3 = 0
        print(l[2])
        for i in l:
            if l[3]+l[4] > maxv3:
                maxv3 = l[3]+l[4]


print('maxball sredi 8')
print(maxv)
print('maxball sredi 9')
print(maxv1)
print('maxball sredi 10')
print(maxv2)
print('maxball sredi 11')
print(maxv3)

