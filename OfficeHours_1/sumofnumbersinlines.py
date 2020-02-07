# https://informatics.msk.ru/mod/statements/view3.php?id=5763&chapterid=111333#1

a = open('input.txt', 'r').readlines()
b = open('output.txt', 'w')
for i in range(len(a)):
    sum = 0
    temp = a[i].split()
    for j in range(len(temp)):
        sum += int(temp[j])
    b.write(str(sum) + '\n')