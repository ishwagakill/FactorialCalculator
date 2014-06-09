def factorial(x):
    if x == 0:
        return 1
    else:
        xRange = range(x, 0, -1)
        a = x
        for i in range(0, x-1):
            a = a * xRange[i+1]
        return a

def main():
    print "This is a program that calculates the factorial of the given number."
    while True:
        next = raw_input("> ")
        if next.isdigit():
            break
        else:
            print "Please type a positive integer."
    print factorial(int(next))

if __name__ == "__main__":
    main()
