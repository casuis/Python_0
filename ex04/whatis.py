import sys

def whatis(obj: int):
    if (obj % 2 == 0):
        print("I'm Even.")
    else:
        print("I'm Odd.")
    return

def main():
    try:
        assert len(sys.argv) > 1, "Assertion Error: no argument have been provided, needed one" 
        assert len(sys.argv) == 2, "Assertion Error: more than one argument is provided"
        num = int(sys.argv[1])
    except AssertionError as e:
        print(e)
        return 1
    except ValueError:
        print('Assertion Error: argument is not an integer')

        return 1

    whatis(num)
    return 0

if __name__ == '__main__':
    main()