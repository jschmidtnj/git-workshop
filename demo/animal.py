from sys import argv

def cat():
    print('meow')

def default():
    # hello is default
    print('hello')

def dog():
    print('woof')

def main():
    """
    run the main method
    """
    print('debug print')
    if argv[1] == 'cat':
        cat()
    elif argv[1] == 'dog':
        dog()
    else:
        default()

if __name__ == '__main__':
    main()
