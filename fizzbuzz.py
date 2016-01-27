import sys

def fizzbuzz(i):
    for n in range(i):
        if (n+1) % 2==0 and (n+1) % 3==0:
            print 'fizzbuzz'
        elif (n+1)%2==0:
            print 'fizz'
        elif (n+1)%3==0:
            print 'buzz'
        else:
            print n+1
        

def main():
    if len(sys.argv) != 2:
        print 'usage: ./fizzbuzz.py <number>'
        sys.exit(1)
    
    n = int(sys.argv[1])
    fizzbuzz(n)


if __name__ == '__main__':
    main()