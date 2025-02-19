import sys

def main():
    if (len(sys.argv) < 3):
        raise ValueError('Command and Inputpath is required.')
    command = sys.argv[1]
    inputpath = sys.argv[2]
    if (command == 'reverse'):
        reverse(inputpath)
    elif (command == 'copy'):
        copy(inputpath)
    elif (command == 'duplicate-contents'):
        duplicate_contents(inputpath)
    elif (command == 'replace-string'):
        replace_string(inputpath)
    else:
        raise ValueError('Command is invalid')

def reverse(inputpath):
    print('Reverse', sys.argv)
    outputpath = sys.argv[3]
    with open(inputpath) as f:
        contents = f.read()
        print(f'####### read from {inputpath} #######')
        print(contents)
    with open(outputpath, 'w') as f:
        f.write(contents[::-1])
        print(f'####### write into {outputpath} #######')
        print(contents[::-1])
    print(f'\nReverse successed!! > {outputpath}')

def copy(inputpath):
    print('Copy', sys.argv)
    outputpath = sys.argv[3]
    with open(inputpath) as f:
        contents = f.read()
        print(f'####### read from {inputpath} #######')
        print(contents)
    with open(outputpath, 'w') as f:
        f.write(contents)
        print(f'####### write into {outputpath} #######')
        print(contents)
    print(f'\nCopy successed!! > {outputpath}')

def duplicate_contents(inputpath):
    print('Duplicate_contents', sys.argv)
    n = int(sys.argv[3])
    with open(inputpath) as f:
        contents = f.read()
        print(f'####### read from {inputpath} #######')
        print(contents)
    with open(inputpath, 'a') as f:
        print(f'####### write into {inputpath} #######')
        for _ in range(n):
            f.write(contents)
        print(f'{n} times of {contents}')
    print(f'\nDuplicate_contents successed!! > {inputpath}')

def replace_string(inputpath):
    print('Replace_string', sys.argv)
    needle = sys.argv[3]
    newstring = sys.argv[4]
    with open(inputpath) as f:
        contents = f.read()
        print(f'####### read from {inputpath} #######')
        print(contents)
    with open(inputpath, 'w') as f:
        print(f'####### write into {inputpath} #######')
        print(contents.replace(needle, newstring))
        f.write(contents.replace(needle, newstring))
    print(f'\nReplace_string successed!! > {inputpath}')

main()