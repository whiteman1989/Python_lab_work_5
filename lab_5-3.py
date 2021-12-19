a = [[0,0,0],[0,0,0],[0,0,0]]

n = 3

for i in range(n):
    for j in range(n):
        if i < j:
            a[i][j] = 4
        elif i > j:
            a[i][j] = 5
        else:
            a[i][j] = 3

for line in a:
    print('   '.join(map(str, line)))