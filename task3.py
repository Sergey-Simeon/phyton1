a = input('Введите шестизначный номер билета: ')
part1 = int(a[0]) + int(a[1]) + int(a[2])
part2 = int(a[3]) + int(a[4]) + int(a[5])
if part1 == part2:
    print('YES')
else:
    print('NO')