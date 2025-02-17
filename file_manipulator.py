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
        duplicate_contents()
    elif (command == 'replace-string'):
        replace_string()
    else:
        raise ValueError('Command is invalid')

def reverse(inputpath):
    print('Reverse', sys.argv)
    outputpath = sys.argv[3]
    with open(inputpath) as f:
        contents = f.read()
        print('####### read from ', inputpath)
        print(contents)
    with open(outputpath, 'w') as f:
        f.write(contents[::-1])
        print('####### write into ', outputpath)
        print(contents[::-1])
    print('\nReverse successed!! >', outputpath)

def copy(inputpath):
    print('Copy', sys.argv)
    outputpath = sys.argv[3]
    with open(inputpath) as f:
        contents = f.read()
        print('####### read from ', inputpath)
        print(contents)
    with open(outputpath, 'w') as f:
        f.write(contents)
        print('####### write into ', outputpath)
        print(contents)
    print('\nCopy successed!! >', outputpath)

def duplicate_contents():
    print('Duplicate_contents', sys.argv)

def replace_string():
    print('Replace_string', sys.argv)

main()