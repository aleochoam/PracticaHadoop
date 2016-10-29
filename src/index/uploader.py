import sys

def readfile(name):
    file = open(name, 'r')
    for line in file:
        pair = line.split('\t', 1)
        upload(pair)

def upload(pair):
    //Subir a la base de datos


def main():
    readfile(sys.argv[1])

if __name__ == '__main__':
    main()