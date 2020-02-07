# https://informatics.msk.ru/mod/statements/view3.php?id=5763&chapterid=111327#1

import re

a = open('input.txt', 'r').read().split()
open('output.txt', 'w').write(str(int(a[0]) + int(a[1])))
