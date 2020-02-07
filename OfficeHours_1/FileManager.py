import io 
import os

home = "C:"
current_dir = home 
stack = []
stack.append(current_dir)

def print_dir(current_dir):
    entries = os.listdir(current_dir)
    for i in range (len(entries)):
        print(i + 1, '. ', entries[i], sep='')
    return entries

def parent_dir(current_dir):
    stack.pop()
    current_dir = stack[len(stack) - 1]
    return current_dir

entries = print_dir(home + '/')

while (True):
    print("Please, enter the number of file or directory:")
    selection = input()
    if (selection == 'q'):
        current_dir = parent_dir(current_dir)
        entries = print_dir(current_dir)
    else:
        temp = current_dir + '/' + entries[int(selection) - 1]
        current_dir = temp
        stack.append(temp)
        if (os.path.isdir(current_dir)):
            entries = print_dir(current_dir)
        else:
            f = open(current_dir, 'r')
            print(f.read())
            current_dir = parent_dir(current_dir)
            entries = print_dir(current_dir)