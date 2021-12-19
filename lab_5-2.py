n = 1 # number in grpup

a = [[1,7,n],[8,n,29],[n,2,4]]

print("Вхідні значення матриці: ", a)

for i in range(3):
    for j in range(3):
        a[i][j] = 9

print("Вихідні значення матриці:", a)