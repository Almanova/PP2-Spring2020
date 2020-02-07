# https://informatics.msk.ru/mod/statements/view3.php?id=4663&chapterid=4182#1

import math

n = int(input())
list = []
while n % 2 == 0: 
        list.append(2)
        n = n // 2

for i in range(3, int(math.sqrt(n)) + 1, 2): 
    while n % i== 0: 
        list.append(i)
        n = n // i 
              
if n > 2: 
    list.append(n)

print(*list)