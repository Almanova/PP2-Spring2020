# https://informatics.msk.ru/mod/statements/view3.php?id=5763&chapterid=111328#1

s = open('input.txt', 'r').read()
open('output.txt', 'w').write(s[::-1][1:])