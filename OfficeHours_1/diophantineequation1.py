# https://informatics.msk.ru/mod/statements/view3.php?id=3457&chapterid=3542#1

a = int(input())
b = int(input())
c = int(input())
d = int(input())

for x in range(1001):     
    if a * x**3 + b * x**2 + c * x + d == 0:         
        print(x)