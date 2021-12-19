n = 5 # number in froup

a = [[int(input("Введіть значення для комірки-"+str(j)+" рядку-"+str(i)+": ")) for j in range(3)] for i in range(3)]

print("Матриця:")
for line in a:
    print('   '.join(map(str, line)))

min_value = min([x[1] for x in a])
print("Мінімальне значення другого стовпчика:", min_value )